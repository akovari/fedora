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

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
# We need redis running for some tests
#systemctl start redis
#sed -i 's/port 6379/port 6381/' /etc/redis.conf

pushd .%{gem_install}

#for file in `grep -RE '6381.*rb' %{buildroot}%{gem_dir} | cut -d ':' -f 1`; do sed -i 's/6381/6379/g' $file; done
#sed -i 's|.test/db/redis.sock|/tmp/redis.sock|' test/internals_test.rb

testrb -Ilib test/*_test.rb
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
* Sat Jun 01 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 3.0.4-1
- Initial package
