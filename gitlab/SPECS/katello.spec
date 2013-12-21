# vim: sw=4:ts=4:et
#
# Copyright 2013 Red Hat, Inc.
#
# This software is licensed to you under the GNU General Public
# License as published by the Free Software Foundation; either version
# 2 of the License (GPLv2) or (at your option) any later version.
# There is NO WARRANTY for this software, express or implied,
# including the implied warranties of MERCHANTABILITY,
# NON-INFRINGEMENT, or FITNESS FOR A PARTICULAR PURPOSE. You should
# have received a copy of GPLv2 along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

%if "%{?scl}" == "ruby193"
    %global scl_prefix %{scl}-
    %global scl_ruby /usr/bin/ruby193-ruby
    %global scl_rake /usr/bin/ruby193-rake
%else
    %global scl_ruby /usr/bin/ruby
    %global scl_rake /usr/bin/rake
%endif

%global homedir %{_datarootdir}/%{name}
%global datadir %{_sharedstatedir}/%{name}
%global confdir deploy/common

Name:           katello
Version:        1.4.6
Release:        1%{?dist}
Summary:        A package for managing application life-cycle for Linux systems
BuildArch:      noarch

Group:          Applications/Internet
License:        GPLv2
URL:            http://www.katello.org
Source0:        https://fedorahosted.org/releases/k/a/katello/%{name}-%{version}.tar.gz

Requires:        %{name}-common
Requires:        %{name}-glue-elasticsearch
Requires:        %{name}-glue-pulp
Obsoletes:       %{name}-glue-foreman < 1.3.15
Provides:        %{name}-glue-foreman = 1.3.15
Requires:        %{name}-glue-candlepin
Requires:        %{name}-selinux
Conflicts:       %{name}-headpin
BuildRequires:   %{scl_rake}
Requires:        %{scl_rake}
BuildRequires:   %{scl_ruby}
Requires:        %{scl_ruby}

%description
Provides a package for managing application life-cycle for Linux systems.

%package common
BuildArch:      noarch
Summary:        Common bits for all Katello instances
%if 0%{?fedora} == 18
Requires:       httpd >= 2.4.4
%else
Requires:       httpd
%endif
Requires:       mod_ssl
Requires:       openssl
Requires:       elasticsearch

# service-wait dependency
Requires:       wget
Requires:       curl

Requires:       %{scl_rake}
Requires:       %{scl_ruby}
Requires:       %{?scl_prefix}rubygems
Requires:       %{?scl_prefix}rubygem(rails) >= 3.2.8
Requires:       %{?scl_prefix}rubygem(haml) >= 3.1.2
Requires:       %{?scl_prefix}rubygem(haml-rails)
Requires:       %{?scl_prefix}rubygem(json)
Requires:       %{?scl_prefix}rubygem(rest-client)
Requires:       %{?scl_prefix}rubygem(therubyracer)
Requires:       %{?scl_prefix}v8
Requires:       %{?scl_prefix}rubygem(rails_warden)
Requires:       %{?scl_prefix}rubygem(net-ldap)
Requires:       %{?scl_prefix}rubygem(compass)
Requires:       %{?scl_prefix}rubygem(compass-rails)
Requires:       %{?scl_prefix}rubygem(sass-rails)
Requires:       %{?scl_prefix}rubygem(compass-960-plugin) >= 0.10.4
Requires:       %{?scl_prefix}rubygem(oauth)
Requires:       %{?scl_prefix}rubygem(i18n_data) >= 0.2.6
Requires:       %{?scl_prefix}rubygem(gettext_i18n_rails)
Requires:       %{?scl_prefix}rubygem(simple-navigation) >= 3.3.4
Requires:       %{?scl_prefix}rubygem(pg)
Requires:       %{?scl_prefix}rubygem(delayed_job) >= 3.0.2
Requires:       %{?scl_prefix}rubygem(delayed_job_active_record) >= 0.3.3
Requires:       %{?scl_prefix}rubygem(delayed_job_active_record) < 0.4.0
Requires:       %{?scl_prefix}rubygem(acts_as_reportable) >= 1.1.1
Requires:       %{?scl_prefix}rubygem(ruport) >= 1.7.0
Requires:       %{?scl_prefix}rubygem(prawn)
Requires:       %{?scl_prefix}rubygem(daemons) >= 1.1.4
Requires:       %{?scl_prefix}rubygem(uuidtools)
Requires:       %{?scl_prefix}rubygem(hooks)
Requires:       %{?scl_prefix}rubygem(thin)
Requires:       %{?scl_prefix}rubygem(fssm)
Requires:       %{?scl_prefix}rubygem(sass)
Requires:       %{?scl_prefix}rubygem(ui_alchemy-rails) >= 1.0.0
Requires:       %{?scl_prefix}rubygem(chunky_png)
Requires:       %{?scl_prefix}rubygem(tire) >= 0.3.0
Requires:       %{?scl_prefix}rubygem(tire) < 0.4
Requires:       %{?scl_prefix}rubygem(ldap_fluff) >= 0.2.1
Requires:       %{?scl_prefix}rubygem(anemone)
Requires:       %{?scl_prefix}rubygem(apipie-rails) >= 0.0.18
Requires:       %{?scl_prefix}rubygem(logging) >= 1.8.0
Requires:       %{?scl_prefix}rubygem(bundler_ext) >= 0.3
Requires:       %{?scl_prefix}rubygem(rack-openid) >= 1.3.1
Requires:       %{?scl_prefix}rubygem(ruby-openid) >= 2.2.3
Requires:       %{?scl_prefix}rubygem(rabl)
Requires:       %{?scl_prefix}rubygem(dynflow)
Requires:       %{?scl_prefix}rubygem(foreigner)
Requires:       %{?scl_prefix}rubygem(justified)
Requires:       signo >= 0.0.5
Requires:       signo-katello >= 0.0.5
Requires:       lsof

%if 0%{?rhel} == 6
Requires:       redhat-logos >= 60.0.14
%endif

%if 0%{?fedora} > 18
Requires:       %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
%endif

Requires: %{?scl_prefix}ruby

# <workaround> for 714167 - undeclared dependencies (regin & multimap)
# TODO - uncomment the statement once we push patched actionpack to our EL6 repo
#%if 0%{?fedora} && 0%{?fedora} <= 15
Requires:       %{?scl_prefix}rubygem(regin)
#%endif
# </workaround>

Requires(pre):    shadow-utils
Requires(preun):  chkconfig
Requires(preun):  initscripts
Requires(post):   chkconfig
Requires(postun): initscripts coreutils sed

BuildRequires:  coreutils findutils sed
BuildRequires:  %{?scl_prefix}rubygems
BuildRequires:  %{?scl_prefix}rubygem-rake
BuildRequires:  %{?scl_prefix}rubygem(chunky_png)
BuildRequires:  %{?scl_prefix}rubygem(fssm) >= 0.2.7
BuildRequires:  %{?scl_prefix}rubygem(compass)
BuildRequires:  %{?scl_prefix}rubygem(compass-rails)
BuildRequires:  %{?scl_prefix}rubygem(therubyracer)
BuildRequires:  %{?scl_prefix}rubygem(uglifier)
BuildRequires:  %{?scl_prefix}rubygem(sass-rails)
BuildRequires:  %{?scl_prefix}rubygem(compass-960-plugin) >= 0.10.4
BuildRequires:  %{?scl_prefix}rubygem(bundler_ext)
BuildRequires:  %{?scl_prefix}rubygem(logging) >= 1.8.0
BuildRequires:  %{?scl_prefix}rubygem(ui_alchemy-rails) >= 1.0.0
BuildRequires:  %{?scl_prefix}rubygem(rabl)
BuildRequires:  %{?scl_prefix}rubygem(hooks)
BuildRequires:  asciidoc
BuildRequires:  /usr/bin/getopt
BuildRequires:  java >= 0:1.6.0
BuildRequires:  gettext
BuildRequires:  translate-toolkit

%if "%{?scl}" == "ruby193"
BuildRequires: ruby193-build
%endif

# we require this to be able to build api-docs
BuildRequires:       %{?scl_prefix}rubygem(acts_as_reportable) >= 1.1.1
BuildRequires:       %{?scl_prefix}rubygem(apipie-rails) >= 0.0.18
BuildRequires:       %{?scl_prefix}rubygem(daemons) >= 1.1.4
BuildRequires:       %{?scl_prefix}rubygem(gettext_i18n_rails)
BuildRequires:       %{?scl_prefix}rubygem(haml) >= 3.1.2
BuildRequires:       %{?scl_prefix}rubygem(haml-rails)
BuildRequires:       %{?scl_prefix}rubygem(i18n_data) >= 0.2.6
BuildRequires:       %{?scl_prefix}rubygem(json)
BuildRequires:       %{?scl_prefix}rubygem(ldap_fluff)
BuildRequires:       %{?scl_prefix}rubygem(maruku)
BuildRequires:       %{?scl_prefix}rubygem(net-ldap)
BuildRequires:       %{?scl_prefix}rubygem(oauth)
BuildRequires:       %{?scl_prefix}rubygem(pg)
BuildRequires:       %{?scl_prefix}rubygem(prawn)
BuildRequires:       %{?scl_prefix}rubygem(rack-openid) >= 1.3.1
BuildRequires:       %{?scl_prefix}rubygem(rails) >= 3.0.10
BuildRequires:       %{?scl_prefix}rubygem(rails_warden)
BuildRequires:       %{?scl_prefix}rubygem(rest-client)
BuildRequires:       %{?scl_prefix}rubygem(ruby-openid) >= 2.2.3
BuildRequires:       %{?scl_prefix}rubygem(ruport) >= 1.7.0
BuildRequires:       %{?scl_prefix}rubygem(sass)
BuildRequires:       %{?scl_prefix}rubygem(simple-navigation) >= 3.3.4
BuildRequires:       %{?scl_prefix}rubygem(sqlite3)
BuildRequires:       %{?scl_prefix}rubygem(thin)
BuildRequires:       %{?scl_prefix}rubygem(tire) < 0.4
BuildRequires:       %{?scl_prefix}rubygem(tire) >= 0.3.0
BuildRequires:       %{?scl_prefix}rubygem(uuidtools)

%description common
Common bits for all Katello instances

%package all
BuildArch:      noarch
Summary:        A meta-package to pull in all components for Katello
Requires:       %{name}
Requires:       %{name}-configure
Requires:       %{name}-cli
Requires:       postgresql-server
Requires:       postgresql

%if 0%{?fedora} > 18
Requires(post): candlepin-tomcat
%else
Requires(post): candlepin-tomcat6
%endif

Requires:       candlepin-selinux
# the following backend engine deps are required by <katello-configure>
Requires:       mongodb
Requires:       mongodb-server
Requires:       v8
Requires:       qpid-cpp-server
Requires:       qpid-cpp-client
Requires:       qpid-cpp-client-ssl
Requires:       qpid-cpp-server-ssl
# </katello-configure>


%description all
This is the Katello meta-package.  If you want to install Katello and all
of its dependencies on a single machine, you should install this package
and then run katello-configure to configure everything.

%package foreman-all
BuildArch:      noarch
Summary:        A meta-package to pull in all components for Katello and Foreman
Requires:       %{name}-all
Requires:       %{name}-configure-foreman
Requires:       %{name}-configure-foreman-proxy

%description foreman-all

This is a meta-package for Katello-Foreman integration. If you want to
install Katello and all of its dependencies, including Foreman, on a
single machine, you should install this package and then run
katello-configure to configure everything.


%package glue-elasticsearch
BuildArch:      noarch
Summary:         Katello connection classes for the Elastic Search backend
Requires:        %{name}-common

%description glue-elasticsearch
Katello connection classes for the Elastic Search backend

%package glue-pulp
BuildArch:      noarch
Summary:         Katello connection classes for the Pulp backend
Requires:        %{name}-common
Requires:        pulp-server
Requires:        pulp-rpm-plugins
Requires:        pulp-katello-plugins
Requires:        pulp-selinux
Requires:        pulp-puppet-plugins
Requires:        pulp-nodes-parent
Requires:        createrepo >= 0.9.9-18%{?dist}
Requires:        %{?scl_prefix}rubygem(runcible) >= 1.0.0

%description glue-pulp
Katello connection classes for the Pulp backend

%package glue-candlepin
BuildArch:      noarch
Summary:         Katello connection classes for the Candlepin backend
Requires:        %{name}-common

%description glue-candlepin
Katello connection classes for the Candlepin backend

%package headpin
Summary:        A subscription management only version of Katello
BuildArch:      noarch
Requires:       katello-common
Requires:       %{name}-glue-candlepin
Requires:       %{name}-glue-elasticsearch
Requires:       katello-selinux
Requires:       %{?scl_prefix}rubygem(bundler_ext)
Requires:       %{scl_rake}
Requires:       %{scl_ruby}

%description headpin
A subscription management only version of Katello.

%package headpin-all
Summary:        A meta-package to pull in all components for katello-headpin
Requires:       katello-headpin
Requires:       katello-configure
Requires:       katello-cli
Requires:       postgresql-server
Requires:       postgresql
Requires(post): candlepin-tomcat6
Requires:       candlepin-selinux
Requires:       thumbslug
Requires:       thumbslug-selinux

%description headpin-all
This is the Katello-headpin meta-package.  If you want to install Headpin and all
of its dependencies on a single machine, you should install this package
and then run katello-configure to configure everything.

%package api-docs
Summary:         Documentation files for Katello API
BuildArch:       noarch
Requires:        %{name}-common

%description api-docs
Documentation files for Katello API.

%package headpin-api-docs
Summary:         Documentation files for Headpin API
BuildArch:       noarch
Requires:        %{name}-common

%description headpin-api-docs
Documentation files for Headpin API.

# <devel packages are not SCL enabled yet - not avaiable on SCL platforms>
%if %{?scl:0}%{!?scl:1}

%package devel-all
Summary:         Katello devel support (all subpackages)
BuildArch:       noarch
Requires:        %{name}-devel = %{version}-%{release}
Requires:        %{name}-devel-profiling = %{version}-%{release}
Requires:        %{name}-devel-test = %{version}-%{release}
Requires:        %{name}-devel-checking = %{version}-%{release}
Requires:        %{name}-devel-coverage = %{version}-%{release}
Requires:        %{name}-devel-debugging = %{version}-%{release}

%description devel-all
Meta package to install all %{name}-devel-* subpackages.

%package devel
Summary:         Katello devel support
BuildArch:       noarch
Requires:        %{name} = %{version}-%{release}
# Gemfile
Requires:        rubygem(ci_reporter) >= 1.6.3
# dependencies from bundler.d/development.rb
Requires:        rubygem(rspec-rails) >= 2.0.0
Requires:        rubygem(parallel_tests)
Requires:        rubygem(yard) >= 0.5.3
Requires:        rubygem(js-routes)
Requires:        rubygem(gettext) >= 1.9.3
Requires:        rubygem(ruby_parser)
Requires:        rubygem(sexp_processor)
Requires:        rubygem(factory_girl_rails) >= 1.4.0
# dependencies from bundler.d/development_boost.rb
Requires:        rubygem(rails-dev-boost)
# dependencies from bundler.d/apipie.rb
Requires:        rubygem(maruku)

%description devel
Rake tasks and dependecies for Katello developers

%package devel-profiling
Summary:         Katello devel support (profiling)
BuildArch:       noarch
Requires:        %{name} = %{version}-%{release}
# dependencies from bundler.d/optional.rb
Requires:        rubygem(ruby-prof)
Requires:        rubygem(newrelic_rpm)

%description devel-profiling
Rake tasks and dependecies for Katello developers, which enables
profiling.

%package devel-checking
Summary:         Katello devel support (unit test and syntax checking)
BuildArch:       noarch
Provides:        katello-devel-jshintrb = 1.2.1-1
Obsoletes:       katello-devel-jshintrb < 1.2.1-1
Requires:        %{name} = %{version}-%{release}
# dependencies from bundler.d/checking.rb
Requires:        rubygem(therubyracer)
Requires:        rubygem(ref)
Requires:        rubygem(jshintrb)

%description devel-checking
Rake tasks and dependecies for Katello developers, which enables
syntax checking and is need for unit testing.

%package devel-coverage
Summary:         Katello devel support (test coverage utils)
BuildArch:       noarch
Requires:        %{name} = %{version}-%{release}
# dependencies from bundler.d/coverage.rb
Requires:        rubygem(simplecov)

%description devel-coverage
Rake tasks and dependecies for Katello developers, which enables
code coverage for tests.

%package devel-debugging
Summary:         Katello devel support (debugging)
BuildArch:       noarch
Requires:        %{name} = %{version}-%{release}
# dependencies from bundler.d/debugging.rb
Requires:        rubygem(ruby-debug19)

%description devel-debugging
Rake tasks and dependecies for Katello developers, which enables
debugging Ruby code.

%package devel-test
Summary:         Katello devel support (testing)
BuildArch:       noarch
Requires:        %{name} = %{version}-%{release}
Requires:        %{name}-devel = %{version}-%{release}
Requires:        rubygem(ZenTest) >= 4.4.0
Requires:        rubygem(autotest-rails) >= 4.1.0
Requires:        rubygem(rspec-rails) >= 2.0.0
Requires:        rubygem(webrat) >= 0.7.3
Requires:        rubygem(nokogiri) >= 0.9.9
Requires:        rubygem(vcr)
Requires:        rubygem(webmock)

%description devel-test
Rake tasks and dependecies for Katello developers, which enables
testing.

# </devel packages are not SCL enabled yet - not avaiable on SCL platforms>
%endif

%prep
%setup -q

%build
export RAILS_ENV=build

#don't distribute quiet_paths
rm -f config/initializers/quiet_paths.rb
rm -f lib/tasks/test.rake
rm -f bundler.d/test.rb
rm -f db/.rubocop.yml
rm -f .rubocop.yml

# when running in SCL we do not distribute any devel packages yet
%if %{?scl:1}%{!?scl:0}
    rm -f bundler.d/checking.rb
    rm -f bundler.d/coverage.rb
    rm -f bundler.d/debugging.rb
    rm -f bundler.d/development.rb
    rm -f bundler.d/development_boost.rb
    rm -f bundler.d/optional.rb
    rm -rf bundler.d/assets.rb
%endif

%if %{?scl:1}%{!?scl:0}
    #replace shebangs for SCL
    find script/ -type f | xargs sed -ri '1sX(/usr/bin/ruby|/usr/bin/env ruby)X%{scl_ruby}X'
    #use rake from SCL
    sed -ri 'sX(/usr/bin/rake|/usr/bin/env rake)X%{scl_rake}Xg' script/katello-refresh-cdn
%endif

# touch the katello yml for bundler ext stuff
touch config/katello.yml

#check and generate gettext MO files
make -C locale check all-mo %{?_smp_mflags}
# | sed -e '/Warning: obsolete msgid exists./,+1d' | sed -e '/Warning: fuzzy message was ignored./,+1d'

#use Bundler_ext instead of Bundler
mv Gemfile Gemfile.in

#pull in branding if present
if [ -d branding ] ; then
  cp -r branding/* .
fi

%if ! 0%{?fastbuild:1}
    #compile SASS files
    echo Compiling Assets...
    mv lib/tasks lib/tasks_disabled
    export BUNDLER_EXT_NOSTRICT=1
    export BUNDLER_EXT_GROUPS="default assets"
%{?scl:scl enable %{scl} - << \EOF}
    rake  assets:precompile:primary --trace RAILS_ENV=production
    rake  assets:precompile:nondigest --trace
%{?scl:EOF}
    rm config/katello.yml
    mv lib/tasks_disabled lib/tasks
%endif

#man pages
a2x -d manpage -f manpage man/katello-service.8.asciidoc

#api docs
%if ! 0%{?nodoc:1}
    # we need to rename all the extra tasks because we do not have all the dependencies, we
    # don't need them and there is no way to disable this via a rake option
    mv lib/tasks lib/tasks_disabled
    # by default do not stop on missing dep and only require "build" environment
    export BUNDLER_EXT_NOSTRICT=1
    export BUNDLER_EXT_GROUPS="default build"
    export RAILS_ENV=build
    touch config/katello.yml
%{?scl:scl enable %{scl} "}
    rake apipie:static apipie:cache --trace
%{?scl:"}

    # API doc for Headpin mode
    echo "common:" > config/katello.yml
    echo "  app_mode: headpin" >> config/katello.yml
%{?scl:scl enable %{scl} "}
    rake apipie:static apipie:cache OUT=doc/headpin-apidoc --trace
%{?scl:"}
    rm -rf config/katello.yml db/build.sqlite3 db/openid-store
    mv lib/tasks_disabled lib/tasks
%endif

%install
#prepare dir structure
install -d -m0755 %{buildroot}%{homedir}
install -d -m0755 %{buildroot}%{datadir}
install -d -m0755 %{buildroot}%{datadir}/tmp
install -d -m0755 %{buildroot}%{datadir}/tmp/pids
install -d -m0755 %{buildroot}%{datadir}/config
install -d -m0755 %{buildroot}%{_sysconfdir}/%{name}
install -d -m0755 %{buildroot}%{datadir}/openid-store
install -d -m0755 %{buildroot}%{datadir}/openid-store/associations
install -d -m0755 %{buildroot}%{datadir}/openid-store/nonces
install -d -m0755 %{buildroot}%{datadir}/openid-store/temp

install -d -m0755 %{buildroot}%{_localstatedir}/log/%{name}
mkdir -p %{buildroot}/%{_mandir}/man8

# clean the application directory before installing
[ -d tmp ] && rm -rf tmp

# remove build gem group
rm -f bundler.d/build.rb

# copy the application to the target directory
# note that locale is listed here, which copies po files
mkdir .bundle
cp -R .bundle Gemfile.in bundler.d Rakefile app autotest ca config config.ru db lib locale public script spec vendor engines %{buildroot}%{homedir}
rm -f {buildroot}%{homedir}/script/katello-reset-dbs

# do not copy mo files for now, per tom
##copy MO files
#pushd locale
#for MOFILE in $(find . -name "*.mo"); do
#    DIR=$(dirname "$MOFILE")
#    install -d -m 0755 %{buildroot}%{_datadir}/katello/locale/$DIR
#    install -d -m 0755 %{buildroot}%{_datadir}/katello/locale/$DIR/LC_MESSAGES
#    install -m 0644 $DIR/*.mo %{buildroot}%{_datadir}/katello/locale/$DIR/LC_MESSAGES
#done
#popd

#copy configs and other var files (will be all overwriten with symlinks)
touch %{buildroot}%{_sysconfdir}/%{name}/%{name}.yml
chmod 600 %{buildroot}%{_sysconfdir}/%{name}/%{name}.yml
install -m 644 config/environments/production.rb %{buildroot}%{_sysconfdir}/%{name}/environment.rb

#copy cron scripts to be scheduled daily
install -d -m0755 %{buildroot}%{_sysconfdir}/cron.daily
install -m 755 script/katello-refresh-cdn %{buildroot}%{_sysconfdir}/cron.daily/katello-refresh-cdn

#create apache config templates
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.d
echo "# this file will be overwritten by running katello-configure" > %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.d/%{name}.conf

#copy init scripts and sysconfigs
install -Dp -m0644 %{confdir}/%{name}.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -Dp -m0644 %{confdir}/service-wait.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/service-wait
install -Dp -m0755 %{confdir}/%{name}.init %{buildroot}%{_initddir}/%{name}
install -Dp -m0755 %{confdir}/%{name}-jobs.init %{buildroot}%{_initddir}/%{name}-jobs
install -Dp -m0644 %{confdir}/%{name}.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -Dp -m0644 %{confdir}/%{name}.httpd.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf
install -Dp -m0644 %{confdir}/thin.yml %{buildroot}%{_sysconfdir}/%{name}/
install -Dp -m0644 %{confdir}/mapping.yml %{buildroot}%{_sysconfdir}/%{name}/

#overwrite config files with symlinks to /etc/katello
ln -svf %{_sysconfdir}/%{name}/%{name}.yml %{buildroot}%{homedir}/config/%{name}.yml
#ln -svf %{_sysconfdir}/%{name}/database.yml %{buildroot}%{homedir}/config/database.yml
ln -svf %{_sysconfdir}/%{name}/environment.rb %{buildroot}%{homedir}/config/environments/production.rb
install -p -m0644 etc/service-list %{buildroot}%{_sysconfdir}/%{name}/

#create symlinks for some db/ files
ln -svf %{datadir}/schema.rb %{buildroot}%{homedir}/db/schema.rb
ln -svf %{datadir}/openid-store %{buildroot}%{homedir}/db/openid-store

#create symlinks for data
ln -sv %{_localstatedir}/log/%{name} %{buildroot}%{homedir}/log
ln -sv %{datadir}/tmp %{buildroot}%{homedir}/tmp

#create symlinks for important scripts
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sbindir}
ln -sv %{homedir}/script/katello-debug %{buildroot}%{_bindir}/katello-debug
ln -sv %{homedir}/script/katello-generate-passphrase %{buildroot}%{_bindir}/katello-generate-passphrase
ln -sv %{homedir}/script/katello-service %{buildroot}%{_bindir}/katello-service
ln -sv %{homedir}/script/service-wait %{buildroot}%{_sbindir}/service-wait

#re-configure database to the /var/lib/katello directory
sed -Ei 's/\s*database:\s+db\/(.*)$/  database: \/var\/lib\/katello\/\1/g' %{buildroot}%{homedir}/config/database.yml

#remove files which are not needed in the homedir
rm -f %{buildroot}%{homedir}/lib/tasks/.gitkeep
rm -f %{buildroot}%{homedir}/vendor/plugins/.gitkeep

#branding
if [ -d branding ] ; then
  ln -svf %{_datadir}/icons/hicolor/24x24/apps/system-logo-icon.png %{buildroot}%{homedir}/public/images/rh-logo.png
  ln -svf %{_sysconfdir}/favicon.png %{buildroot}%{homedir}/public/images/embed/favicon.png
  rm -rf %{buildroot}%{homedir}/branding
fi

#correct permissions
find %{buildroot}%{homedir} -type d -print0 | xargs -0 chmod 755
find %{buildroot}%{homedir} -type f -print0 | xargs -0 chmod 644
chmod +x %{buildroot}%{homedir}/script/*
chmod a+r %{buildroot}%{homedir}/ca/redhat-uep.pem

# install man page
install -m 644 man/katello-service.8 %{buildroot}/%{_mandir}/man8

%post common

#Add /etc/rc*.d links for the script
/sbin/chkconfig --add %{name}
/sbin/chkconfig --add %{name}-jobs

#Generate secret token if the file does not exist
#(this must be called both for installation and upgrade)
TOKEN=/etc/katello/secret_token
# this file must not be world readable at generation time
umask 0077
test -f $TOKEN || (echo $(</dev/urandom tr -dc A-Za-z0-9 | head -c128) > $TOKEN \
    && chmod 600 $TOKEN && chown katello:katello $TOKEN)

%posttrans common
/sbin/service %{name} condrestart >/dev/null 2>&1 || :

%post headpin-all
usermod -a -G katello-shared tomcat

%post all
usermod -a -G katello-shared tomcat

%files
### if you put something here and it should go to headpin as well
### then add it to "files headpin" section few pages below too
%attr(600, katello, katello)
%{_bindir}/katello-*
%ghost %attr(600, katello, katello) %{_sysconfdir}/%{name}/secret_token
%dir %{homedir}/app
%{homedir}/app/controllers
%{homedir}/app/helpers
%{homedir}/app/mailers
%dir %{homedir}/app/models
%{homedir}/app/models/*.rb
%{homedir}/app/models/authorization/*.rb
%{homedir}/app/models/candlepin
%{homedir}/app/models/ext
%{homedir}/app/models/roles_permissions
%{homedir}/app/assets/
%{homedir}/vendor
%{homedir}/app/views
%{homedir}/autotest
%{homedir}/ca
%{homedir}/config
%{homedir}/db/migrate/
%{homedir}/db/products.json
%{homedir}/db/seeds.rb
%{homedir}/lib/*.rb
%{homedir}/lib/katello/
%exclude %{homedir}/lib/README
%{homedir}/app/lib/*.rb
%exclude %{homedir}/app/lib/README
%dir %{homedir}/app/lib/glue
%{homedir}/app/lib/glue/*.rb
%{homedir}/lib/monkeys
%{homedir}/app/lib/navigation
%{homedir}/app/lib/notifications
%{homedir}/app/lib/validators
%{homedir}/app/lib/api
%{homedir}/app/lib/dashboard

%dir %{homedir}/app/lib/resources
%{homedir}/app/lib/content_search
%{homedir}/lib/tasks
%exclude %{homedir}/lib/tasks/yard.rake
%exclude %{homedir}/lib/tasks/hudson.rake
%exclude %{homedir}/lib/tasks/jsroutes.rake
%exclude %{homedir}/lib/tasks/jshint.rake
%exclude %{homedir}/lib/tasks/simplecov.rake
%exclude %{homedir}/script/pulp_integration_tests
%{homedir}/locale
%{homedir}/public
%if ! 0%{?nodoc:1}
%exclude %{homedir}/public/apipie-cache
%endif
%{homedir}/script
%exclude %{homedir}/script/service-wait
%{homedir}/spec
%{homedir}/tmp
%dir %{homedir}/.bundle
%{homedir}/config.ru
%{homedir}/Gemfile.in
%config(noreplace) %{_sysconfdir}/%{name}/service-list
%{homedir}/Rakefile
%{_mandir}/man8/katello-service.8*
### if you put something here and it should go to headpin as well
### then add it to "files headpin" section few pages below too

%files common
%doc LICENSE.txt
%{_sbindir}/service-wait
%dir %{_sysconfdir}/%{name}
%config(noreplace) %attr(600, katello, katello) %{_sysconfdir}/%{name}/%{name}.yml
%config(noreplace) %{_sysconfdir}/%{name}/thin.yml
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%dir %{_sysconfdir}/httpd/conf.d/katello.d
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.d/%{name}.conf
%config %{_sysconfdir}/%{name}/environment.rb
%config %{_sysconfdir}/logrotate.d/%{name}
%config %{_sysconfdir}/%{name}/mapping.yml
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/service-wait
%{_initddir}/%{name}
%{_initddir}/%{name}-jobs
%{homedir}/log
%dir %{homedir}/db
%{homedir}/db/schema.rb
%dir %{homedir}/lib
%dir %{homedir}/app/lib
%dir %{homedir}/app/lib/resources
%{homedir}/app/lib/resources/cdn.rb
%{homedir}/lib/headpin
%{homedir}/lib/util
%{homedir}/app/lib/util
%{homedir}/script/service-wait
%{homedir}/db/openid-store
%attr(755, katello, katello) %{datadir}/openid-store/associations
%attr(755, katello, katello) %{datadir}/openid-store/nonces
%attr(755, katello, katello) %{datadir}/openid-store/temp
#Engine files
%dir %{homedir}/engines/fort
%{homedir}/engines/fort/app
%{homedir}/engines/fort/config
%{homedir}/engines/fort/fort.gemspec
%{homedir}/engines/fort/Gemfile
%{homedir}/engines/fort/db
%{homedir}/engines/fort/lib
%{homedir}/engines/fort/README.rdoc
%exclude %{homedir}/engines/fort/test
%exclude %{homedir}/engines/fort/script
%exclude %{homedir}/engines/fort/Rakefile
%exclude %{homedir}/engines/fort/LICENSE.txt
%exclude %{homedir}/engines/fort/.gitignore
%dir %{homedir}/engines/bastion
%{homedir}/engines/bastion/bastion.gemspec
%{homedir}/engines/bastion/README.md
%{homedir}/engines/bastion/app
%{homedir}/engines/bastion/lib
%{homedir}/engines/bastion/vendor/assets/components
%exclude %{homedir}/engines/bastion/bower.json
%exclude %{homedir}/engines/bastion/Gruntfile.js
%exclude %{homedir}/engines/bastion/karma.conf.js
%exclude %{homedir}/engines/bastion/package.json
%exclude %{homedir}/engines/bastion/.bowerrc
%exclude %{homedir}/engines/bastion/.jshintrc
%exclude %{homedir}/engines/bastion/.gitignore
%exclude %{homedir}/engines/bastion/test


%defattr(-, katello, katello)
%dir %{homedir}
%attr(750, katello, katello) %{_localstatedir}/log/%{name}
%{datadir}
%ghost %attr(640, katello, katello) %{_localstatedir}/log/%{name}/production.log
%ghost %attr(640, katello, katello) %{_localstatedir}/log/%{name}/delayed_production.log

%files glue-elasticsearch
%{homedir}/app/models/glue/elastic_search

%files glue-pulp
%{homedir}/bundler.d/pulp.rb
%{homedir}/app/models/glue/pulp
%config(missingok) %{_sysconfdir}/cron.daily/katello-refresh-cdn

%files glue-candlepin
%{homedir}/app/models/glue/candlepin
%{homedir}/app/models/glue/provider.rb
%{homedir}/app/lib/resources/candlepin.rb

%files all

%files foreman-all

%files headpin
%attr(600, katello, katello)
%{_bindir}/katello-*
%dir %{homedir}/app
%{homedir}/app/controllers
%{homedir}/app/helpers
%{homedir}/app/mailers
%{homedir}/app/models
%exclude %{homedir}/app/models/glue/*
%exclude %{homedir}/lib/tasks/simplecov.rake
%{homedir}/app/assets/
%{homedir}/vendor
%{homedir}/app/views
%{homedir}/autotest
%{homedir}/ca
%{homedir}/config
%{homedir}/db/migrate/
%{homedir}/db/products.json
%{homedir}/db/seeds.rb
%{homedir}/lib/*.rb
%{homedir}/lib/katello/
%exclude %{homedir}/lib/README
%{homedir}/app/lib/*.rb
%exclude %{homedir}/app/lib/README
%{homedir}/lib/monkeys
%{homedir}/app/lib/navigation
%{homedir}/app/lib/notifications
%{homedir}/app/lib/validators
%{homedir}/app/lib/api
%{homedir}/app/lib/dashboard
%exclude %{homedir}/app/lib/resources/candlepin.rb
%{homedir}/lib/tasks
%{homedir}/lib/util
%{homedir}/app/lib/util
%{homedir}/app/lib/glue/event.rb
%{homedir}/app/lib/glue/queue.rb
%{homedir}/app/lib/glue/task.rb
%{homedir}/locale
%{homedir}/public
%if ! 0%{?nodoc:1}
%exclude %{homedir}/public/apipie-cache
%endif
%{homedir}/script
%{homedir}/spec
%{homedir}/tmp
%{homedir}/.bundle
%{homedir}/config.ru
%{homedir}/Gemfile.in
%{homedir}/Rakefile

%files headpin-all

%files api-docs
%if ! 0%{?nodoc:1}
%doc doc/apidoc*
%{homedir}/public/apipie-cache
%endif

%files headpin-api-docs
%if ! 0%{?nodoc:1}
%doc doc/headpin-apidoc*
%{homedir}/public/headpin-apipie-cache
%endif

# <devel packages are not SCL enabled yet - not avaiable on SCL platforms>
%if %{?scl:0}%{!?scl:1}

%files devel-all

%files devel
%{homedir}/bundler.d/development.rb
%{homedir}/bundler.d/assets.rb
%{homedir}/bundler.d/development_boost.rb
%{homedir}/lib/tasks/yard.rake
%{homedir}/lib/tasks/hudson.rake
%{homedir}/lib/tasks/jsroutes.rake

%files devel-profiling
%{homedir}/bundler.d/optional.rb

%files devel-test
%{homedir}/lib/tasks/simplecov.rake
%{homedir}/script/pulp_integration_tests

%files devel-checking
%{homedir}/bundler.d/checking.rb
%{homedir}/lib/tasks/jshint.rake

%files devel-coverage
%{homedir}/bundler.d/coverage.rb

%files devel-debugging
%{homedir}/bundler.d/debugging.rb

# </devel packages are not SCL enabled yet - not avaiable on SCL platforms>
%endif

%pre common
# Add the "katello" user and group
getent group %{name} >/dev/null || groupadd -r %{name} -g 182
getent passwd %{name} >/dev/null || \
    useradd -r -g %{name} -d %{homedir} -u 182 -s /sbin/nologin -c "Katello" %{name}
# add tomcat & katello to the katello shared group for reading sensitive files
getent group katello-shared > /dev/null || groupadd -r katello-shared
usermod -a -G katello-shared katello
exit 0

%preun common
if [ $1 -eq 0 ] ; then
    /sbin/service %{name}-jobs stop >/dev/null 2>&1
    /sbin/chkconfig --del %{name}-jobs
    /sbin/service %{name} stop >/dev/null 2>&1
    /sbin/chkconfig --del %{name}
fi

%changelog
* Tue Sep 03 2013 Partha Aji <paji@redhat.com> 1.4.6-1
- Updated spec to deal with renaming of cp tomcat in f19 (paji@redhat.com)
- Merge pull request #2867 from komidore64/auto-attach-all-systems-notification
  (komidore64@gmail.com)
- Merge pull request #2873 from daviddavis/temp/20130903133042
  (daviddavis@redhat.com)
- Candlepin: Response could be a string; must use present?
  (daviddavis@redhat.com)
- Removing integration_spec folder references from katello.spec
  (daviddavis@redhat.com)
- Merge pull request #2868 from daviddavis/temp/20130903110224
  (daviddavis@redhat.com)
- 987936-link-helper - using search for crosslinking (thomasmckay@redhat.com)
- Merge pull request #2835 from jlsherrill/headpin_fix (jlsherrill@gmail.com)
- Rubocop: Cleaning up helpers (daviddavis@redhat.com)
- Merge pull request #2861 from daviddavis/temp/20130831123621
  (daviddavis@redhat.com)
- Removing integration_spec folder (daviddavis@redhat.com)
- 1002665 - User notification not displayed after running auto attach system
  while running "Auto-attach available subscriptions to all systems"
  (komidore64@gmail.com)
- Merge pull request #2862 from daviddavis/temp/20130831151809
  (daviddavis@redhat.com)
- Rubocop: Fixing app/lib directory (daviddavis@redhat.com)
- Merge pull request #2864 from daviddavis/temp/20130901120718
  (daviddavis@redhat.com)
- Merge pull request #2863 from daviddavis/temp/20130831182736
  (daviddavis@redhat.com)
- Rubocop: Fixing top level models directory (daviddavis@redhat.com)
- Merge pull request #2854 from iNecas/travis-apipie (inecas@redhat.com)
- Rubocop: Fixing the API controllers (daviddavis@redhat.com)
- Rubocop: checking integration_spec folder (daviddavis@redhat.com)
- Merge pull request #2831 from ehelms/product-ui (ericdhelms@gmail.com)
- Bastion: Updates for selecting the newly created provider and cleanup.
  (ericdhelms@gmail.com)
- Bastion: Adding products table view and creation screen.
  (ericdhelms@gmail.com)
- Test ability to generate apipie doc from travis (inecas@redhat.com)
- including engine files in katello-common for headpin (jsherril@redhat.com)

