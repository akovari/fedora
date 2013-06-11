#!/bin/bash

file_raw='/home/axil/fedora/gitlab-deps/rubygems_fedora_raw'
file_new='/home/axil/fedora/gitlab-deps/rubygems_fedora'

touch $file_raw
yum search all rubygem | awk '{print $1}' > $file_raw

sed -e 's/rubygem-//g' -e 's/.noarch//g' -e 's/.x86_64//g' -e '/-doc/d' -e '/i686/d' -e '/==/d' -e '/:/d' < $file_raw > $file_new

