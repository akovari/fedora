# Generated from redis-rack-1.4.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name redis-rack

Name: rubygem-%{gem_name}
Version: 1.4.2
Release: 1%{?dist}
Summary: Redis Store for Rack
Group: Development/Languages
License: MIT
URL: https://github.com/jodosha/redis-store/tree/master/redis-rack
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(redis-store) => 1.1.0
Requires: rubygem(redis-store) < 1.2
Requires: rubygem(rack) => 1.4.1
Requires: rubygem(rack) < 1.5
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: rubygem(rack) => 1.4.1
BuildRequires: rubygem(test-unit)
#BuildRequires: rubygem(mocha)
#BuildRequires: rubygem(test-helper)
#BuildRequires: rubygem(minitest)
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Redis Store for Rack

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

# %%gem_install compiles any C extensions and installs the gem into ./%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
#sed -i '/Bundler/d' test/test_helper.rb
#testrb2 -Ilib test/
popd


%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/MIT-LICENSE
%{gem_spec}
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/test/
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Sat Aug 10 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 1.4.2-1
- Initial package
