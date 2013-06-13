#!/bin/bash

fedora_gems_raw='/home/axil/fedora/gitlab-deps/rubygems_fedora_raw'
fedora_gems_new='/home/axil/fedora/gitlab-deps/rubygems_fedora'
bugzilla_gems_raw='/home/axil/fedora/gitlab-deps/rubygems_bugzilla_raw'
bugzilla_gems='/home/axil/fedora/gitlab-deps/rubygems_bugzilla'

echo 'Searching Fedora repositories...'
touch $fedora_gems_raw
yum search all rubygem | awk '{print $1}' > $fedora_gems_raw

# Striping uneeded symbols and the rubygem- prefix
sed -e 's/rubygem-//g' -e 's/.noarch//g' -e 's/.x86_64//g' -e '/-doc/d' -e '/i686/d' -e '/==/d' -e '/:/d' < $fedora_gems_raw > $fedora_gems_new

# Install python-bugzilla first
echo 'Searching Bugzilla for Review Requests...'
bugzilla query --product=fedora --bug_status=new,assigned --component='Package Review' --short_desc='rubygem-' \
  | awk 'BEGIN { FS = " - " } ; { print $3 }' | awk 'BEGIN { FS = ":" } ; { print $2 }' | sed -e 's/ rubygem-//' >> $fedora_gems_new

bugzilla query --product=fedora --bug_status=new,assigned --component='Package Review' --short_desc='rubygem-' \
  | awk 'BEGIN { FS = " - " } ; { print $3 }' | awk 'BEGIN { FS = ":" } ; { print $2 }' | sed -e 's/ rubygem-//' > $bugzilla_gems

echo 'Done!'
