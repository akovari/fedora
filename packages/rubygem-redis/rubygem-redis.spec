# Generated from redis-3.0.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name redis

Name: rubygem-%{gem_name}
Version: 3.0.4
Release: 2%{?dist}
Summary: A Ruby client library for Redis
Group: Development/Languages
License: MIT
URL: https://github.com/redis/redis-rb
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
BuildRequires: ruby 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: rubygem(minitest) 
BuildRequires: redis
BuildRequires: nmap-ncat
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
A Ruby client that tries to match Redis' API one-to-one, while still
providing an idiomatic interface. It features thread-safety,
client-side sharding, pipelining, and an obsession for performance.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
gem unpack %{SOURCE0}

%setup -q -T -D -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%check
pushd .%{gem_instdir}

## Redis doesn't support IPv6 yet and localhost resolves to IPv6 address.
## Use 127.0.0.1 instead or else it hangs while testing.
## https://bugzilla.redhat.com/show_bug.cgi?id=978284#c2
sed -i "s/localhost/127.0.0.1/" test/publish_subscribe_test.rb

## Start a testing redis server instance
/usr/sbin/redis-server test/test.conf

## Set locale because two tests fail in mock.
## https://github.com/redis/redis-rb/issues/345
LANG=en_US.utf8 

testrb -Ilib test/*_test.rb

## Kill redis-server
kill -INT `cat test/db/redis.pid`
popd

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/LICENSE
%{gem_spec}
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/test/db/.gitignore

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/Rakefile
%{gem_instdir}/benchmarking/
%{gem_instdir}/examples/
%{gem_instdir}/test/

%changelog
* Thu Jun 27 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 3.0.4-2
- Fix failing test
- Remove redis from Requires
- Exclude dot file

* Sun Jun 23 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 3.0.4-1
- Initial package
