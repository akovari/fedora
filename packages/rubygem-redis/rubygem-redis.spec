# Generated from redis-3.0.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name redis

Name: rubygem-%{gem_name}
Version: 3.0.4
Release: 1%{?dist}
Summary: A Ruby client library for Redis
Group: Development/Languages
License: MIT
URL: https://github.com/redis/redis-rb
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: redis
BuildRequires: ruby 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: rubygem(minitest) 
BuildRequires: redis
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

%setup -q -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%check

## We need redis running for some tests.
## Is this the right way to do it?
#systemctl start redis

pushd .%{gem_instdir}

## Test requires redis listening on port 6381 whereas in Fedora 
## we have 6379 set as default. Change that port in test file.
sed -i 's|6381|6379|' test/helper.rb

testrb -Ilib test/*_test.rb
popd

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/Rakefile
%doc %{gem_instdir}/examples
%doc %{gem_instdir}/test
%doc %{gem_instdir}/benchmarking

%changelog
* Sat Jun 19 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 3.0.4-1
- Initial package
