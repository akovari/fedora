#!/usr/bin/env python2

import json
import urllib2
import re
import os
import pkgwat.api

def gitlab_gems_all():
  '''file -> list

  Returns a sorted list of Gitlab's dependencies included in Gemfile.lock.

  '''
  gemfile_gitlab = urllib2.urlopen('https://raw.github.com/gitlabhq/gitlabhq/master/Gemfile.lock')
  gemfile_gitlab_shell = urllib2.urlopen('https://raw.github.com/gitlabhq/gitlab-shell/master/Gemfile.lock')

  gem_gitlab = gemfile_gitlab.readlines()
  gem_shell = gemfile_gitlab_shell.readlines()

  gems = []
  gems = gem_gitlab + gem_shell

  gitlab_gemlist = set()

  for line in gems:
    if line.startswith('  '):
      gitlab_gemlist.add(line.split()[0])
  
  return sorted(gitlab_gemlist)

def gitlab_gems_runtime(gitlab_list):
  '''file -> dictionary

  Returns a sorted list of Gitlab's runtime dependencies.

  '''
  gitlab_dict = {}
  with open(gitlab_list, 'r') as gitlab_file:
    for line in gitlab_file.readlines():
      name = '-'.join(line.split('-')[:-1])
      version = line.split('-')[-1].strip('\n')
      gitlab_dict[name] = version
  
  return gitlab_dict

def fedora_gems_rawhide(file):
  '''file -> dictionary

  Returns a list of rubygems currently packaged in Fedora.
  '''
  fedora_dict = {}

  gemlist = gitlab_gems_runtime(file).keys()

  for gem in gemlist:
    search = pkgwat.api.releases('rubygem-%s' % gem)
    version = search['rows'][0]['stable_version'].split('-')[0]
    fedora_dict[gem] = version

  return fedora_dict
  
def upstream_gems(gitlab_list):
  '''string -> string
  
  Returns the version of a Ruby gem taken from rubygems.org API
  '''
  upstream_dict = {}
  gitlab_list = gitlab_gems_runtime(gitlab_list).keys()
  
  for gem in gitlab_list:
    url = 'https://rubygems.org/api/v1/gems/%s.json' % gem
    js = json.load(urllib2.urlopen(url))
    version = js['version']
    upstream_dict[gem] = version

  return upstream_dict


def find_common(gitlab_gemlist, fedora_gemlist):
  ''' lists -> set

  Returns a set of common items between two lists.

  >>> common_gems(['sinatra', 'sidekiq', 'sass_rails', 'sass'],['sass', 'rspec', 'sass_rails'])
  set(['sass_rails', 'sass'])
  '''
  
  return sorted(set(gitlab_gemlist) & set(fedora_gemlist))

def find_missing(gitlab_gems, common_gems):
  """lists -> list
  
  Returns a list with duplicate items removed. It searches the first list
  and if an item is not in the second list it is added to the new list.
  
  >>> find_missing([1, 2, 3, 4, 5], [2, 4])
  [1, 3, 5]
  """
  missing_gems = []
  for gem in gitlab_gems:
    if gem not in common_gems:
      missing_gems.append(gem)

  return sorted(missing_gems)

def single_gem_dependencies(gem_name):
  '''List dependencies of a gem
  '''
  
  url = 'https://rubygems.org/api/v1/gems/%s.json' % gem_name
  js = json.load(urllib2.urlopen(url))
  deps = js['dependencies']
  runtime_deps = deps['runtime']
  dev_deps =deps['development']

  return runtime_deps

def bugzilla_gems(rubygems_bugzilla_raw):
  """Returns a dictionary with rubygems pending review for Fedora 
  and their status.

  """
  bz_dict = {}
  with open(rubygems_bugzilla_raw, 'r') as f:
    for line in f.readlines():
  
      split_line = re.split(' - ', line)
      strip_rubygem = re.search(r'rubygem-[\w-]+', line).group()
      gem_name = re.sub('rubygem-', '', strip_rubygem)
      bug_id = re.search(r'\d+', line).group()
      status = re.search(r'[A-Z]+', line).group()
      assignee = split_line[1]
      description = split_line[3].strip('\n')
      bz_dict[gem_name] = [bug_id, status, assignee, description]

  return bz_dict


def main():
  
  gitlab_gems_file = os.path.realpath('gitlab53-gems')
  fedora_gems_file = os.path.realpath('rubygems_fedora')
  rubygems_gitlab = os.path.realpath('rubygems_gitlab')
  rubygems_missing = os.path.realpath('rubygems_missing')
  rubygems_common = os.path.realpath('rubygems_common')
  
  print 'Populating GitLab dictionary...'
  gitlab = gitlab_gems_runtime(gitlab_gems_file)
  
  print 'Populating Fedora dictionary...'
  fedora = fedora_gems_rawhide(gitlab_gems_file)

  print 'Populating upstream dictionary...'
  upstream = upstream_gems(gitlab_gems_file)


  print 'Writing GitLab gems to file...'
  gitlab_gems_list = gitlab.keys()
  with open(rubygems_gitlab, 'w') as f:
    for rubygem in gitlab_gems_list:
      f.write(rubygem + '\n')
  
  print 'Writing missing gems to file...'
  missing_gems = find_missing(gitlab_gems_list, sorted(fedora.keys()))
  with open(rubygems_missing, 'w') as f:
    for rubygem in missing_gems:
      f.write(rubygem + '\n')
  
  print 'Calculating common gems...'
  common = find_common(gitlab_gems_list, sorted(fedora.keys()))
  with open(rubygems_common, 'w') as f:
    for rubygem in common:
      f.write(rubygem + '\n')
  
  # Write to a file the gem versions table, wiki styled
  
  print 'Populating versions dictionary...'
  versions = {}
  for gem in gitlab.keys():
    versions[gem] = [gitlab[gem], fedora[gem], upstream[gem]]
  
  versions_table = os.path.realpath('wiki_version_table')
  if os.path.isfile(versions_table):
    print 'Removing old wiki table'
    os.rename(versions_table, versions_table + '.old' )
  
  print 'Writing versions to a wiki table...'
  with open(versions_table, 'a') as f:
    for gem in sorted(gitlab.keys()):
      f.write('|-' + '\n' + '|' + gem + '\n' + '|' + versions[gem][0] + '\n' + '|' + versions[gem][1] + '\n' + '|' + versions[gem][2] + '\n')
  print 'Done!'

  print 'Gitlab uses', len(gitlab_gems_list), 'runtime gems.'
  print 'Fedora has packaged', len(fedora_gems), 'gems.'
  print 'There are', len(common), 'common gems.'
  print 'There should be packaged', len(missing_gems), 'gems.'
  print 'Fedora will have' , round(len(missing_gems)/float(len(fedora_gems))*100,2), '% more ruby packages, that is', len(missing_gems)+len(fedora_gems), 'gems in total.'
  
if __name__ == '__main__':
  main()
