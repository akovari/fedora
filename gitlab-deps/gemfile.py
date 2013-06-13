#!/usr/bin/env python2

import json
import urllib2
#import subprocess

def gitlab_gems_list():
    '''url strings -> list

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
        if line.startswith('    '):
            gitlab_gemlist.add(line.split()[0])
    
    return sorted(gitlab_gemlist)

def fedora_gems_list(fedora_gems_file):
    '''file -> list

    Returns a list of rubygems currently packaged or pending review in Fedora.
    '''
    
    f = open(fedora_gems_file, 'r')
    gemlist = f.read().split('\n')
    f.close()

    return list(set(gemlist))
    
def common_gems(gitlab_gemlist, fedora_gemlist):
    ''' lists -> set

    Returns a set of common items between two lists.

    >>> common_gems(['sinatra', 'sidekiq', 'sass_rails', 'sass'],['sass', 'rspec', 'sass_rails'])
    set(['sass_rails', 'sass'])
    '''
    
    return set(gitlab_gemlist) & set(fedora_gemlist) 

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

    return missing_gems

def gem_dependencies(gem_name):
  '''List dependencies of a gem
  '''
  
  url = 'https://rubygems.org/api/v1/gems/%s.json' % gem_name
  js = json.load(urllib2.urlopen(url))
  deps = js['dependencies']
  runtime_deps = deps['runtime']
  dev_deps = ['development']
  
  return runtime_deps


def statistics(gitlab_gemlist, fedora_gemlist):
    '''
    '''
    pass

def main():
    
    fedora_gems_file = '/home/axil/fedora/gitlab-deps/rubygems_fedora'
    gitlab_gems = gitlab_gems_list()
    fedora_gems = fedora_gems_list(fedora_gems_file)
    common = common_gems(gitlab_gems, fedora_gems)
    missing_gems = find_missing(gitlab_gems, fedora_gems)

    #to_file = raw_input('Save Gitlab\'s deps as: ')
    rubygems_gitlab = '/home/axil/fedora/gitlab-deps/rubygems_gitlab'
    f = open(rubygems_gitlab, 'w')
    for rubygem in gitlab_gems:  
        f.write(rubygem + '\n')
    f.close()
    
    rubygems_missing = '/home/axil/fedora/gitlab-deps/rubygems_missing'
    f = open(rubygems_missing, 'w')
    for rubygem in missing_gems:  
        f.write(rubygem + '\n')
    f.close()
    
    rubygems_common = '/home/axil/fedora/gitlab-deps/rubygems_common'
    f = open(rubygems_common, 'w')
    for rubygem in missing_gems:  
        f.write(rubygem + '\n')
    f.close()
    
    print 'Gitlab uses', len(gitlab_gems), 'gems.'
    print 'Fedora has packaged', len(fedora_gems), 'gems.'
    print 'There are', len(common), 'common gems.'
    print 'There should be packaged', len(gitlab_gems) - len(common), 'gems.'
    print 'Fedora will have' , round((len(gitlab_gems) - len(common))/float(len(fedora_gems))*100,2), '% more ruby packages, that is', len(common)+len(fedora_gems), 'gems in total.'
    
    #for i in common:
    #    print i
if __name__ == '__main__':
    main()
