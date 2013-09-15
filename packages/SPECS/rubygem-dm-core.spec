# Generated from dm-core-1.2.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name dm-core

Name: rubygem-%{gem_name}
Version: 1.2.1
Release: 1%{?dist}
Summary: DataMapper core library
Group: Development/Languages
License: MIT
URL: https://github.com/datamapper/dm-core
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(addressable) => 2.3
Requires: rubygem(addressable) < 3
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: rubygem(rspec) 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
DataMapper core library


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
rspec spec/
popd


%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc

%changelog
* Thu Jul 04 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 1.2.1-1
- Initial package
