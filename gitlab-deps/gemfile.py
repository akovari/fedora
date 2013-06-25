#!/usr/bin/env python2

import json
import urllib2
import re

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

def gitlab_gems_runtime(gitlab_gems):
  '''file -> list

  Returns a sorted list of Gitlab's runtime dependencies.

  '''
  gitlab_dict = {}
  with open(gitlab_gems, 'r') as gitlab_file:
    for line in gitlab_file.readlines():
      gem_name = '-'.join(line.split('-')[:-1])
      gem_ver = line.split('-')[-1].strip('\n')
      gitlab_dict[gem_name] = gem_ver
  
  return gitlab_dict

def fedora_gems_list(fedora_gems_file):
  '''file -> list

  Returns a list of rubygems currently packaged in Fedora.
  '''
  
  with open(fedora_gems_file, 'r') as f:
    gemlist = f.read().split('\n')

  return list(set(gemlist))
  
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
  dev_deps = ['development']
  
  return runtime_deps

def bugzilla_sort_gems(rubygems_bugzilla_raw):
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
  
  fedora_gems_file = '/home/axil/fedora/gitlab-deps/rubygems_fedora'
  fedora_gems = fedora_gems_list(fedora_gems_file)
  gitlab_gems_file = '/home/axil/fedora/gitlab-deps/gitlab53-gems'
  gitlab_gems_list = sorted(gitlab_gems_runtime(gitlab_gems_file).keys())
  common = find_common(gitlab_gems_list, fedora_gems)
  missing_gems = find_missing(gitlab_gems_list, fedora_gems)

  rubygems_gitlab = '/home/axil/fedora/gitlab-deps/rubygems_gitlab'
  with open(rubygems_gitlab, 'w') as f:
    for rubygem in gitlab_gems_list:
      f.write(rubygem + '\n')
  
  rubygems_missing = '/home/axil/fedora/gitlab-deps/rubygems_missing'
  with open(rubygems_missing, 'w') as f:
    for rubygem in missing_gems:
      f.write(rubygem + '\n')
  
  rubygems_common = '/home/axil/fedora/gitlab-deps/rubygems_common'
  with open(rubygems_common, 'w') as f:
    for rubygem in common:
      f.write(rubygem + '\n')
  
  print 'Gitlab uses', len(gitlab_gems_list), 'runtime gems.'
  print 'Fedora has packaged', len(fedora_gems), 'gems.'
  print 'There are', len(common), 'common gems.'
  print 'There should be packaged', len(missing_gems), 'gems.'
  print 'Fedora will have' , round(len(missing_gems)/float(len(fedora_gems))*100,2), '% more ruby packages, that is', len(missing_gems)+len(fedora_gems), 'gems in total.'
  
if __name__ == '__main__':
  main()
