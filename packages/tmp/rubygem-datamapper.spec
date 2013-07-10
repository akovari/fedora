# Generated from datamapper-1.2.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name datamapper

Name: rubygem-%{gem_name}
Version: 1.2.0
Release: 1%{?dist}
Summary: An Object/Relational Mapper for Ruby
Group: Development/Languages
License: 
URL: http://datamapper.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(dm-core) => 1.2.0
Requires: rubygem(dm-core) < 1.3
Requires: rubygem(dm-aggregates) => 1.2.0
Requires: rubygem(dm-aggregates) < 1.3
Requires: rubygem(dm-constraints) => 1.2.0
Requires: rubygem(dm-constraints) < 1.3
Requires: rubygem(dm-migrations) => 1.2.0
Requires: rubygem(dm-migrations) < 1.3
Requires: rubygem(dm-transactions) => 1.2.0
Requires: rubygem(dm-transactions) < 1.3
Requires: rubygem(dm-serializer) => 1.2.0
Requires: rubygem(dm-serializer) < 1.3
Requires: rubygem(dm-timestamps) => 1.2.0
Requires: rubygem(dm-timestamps) < 1.3
Requires: rubygem(dm-validations) => 1.2.0
Requires: rubygem(dm-validations) < 1.3
Requires: rubygem(dm-types) => 1.2.0
Requires: rubygem(dm-types) < 1.3
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Faster, Better, Simpler.


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




%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/Manifest.txt
%doc %{gem_instdir}/README.txt

%changelog
* Thu Jul 04 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 1.2.0-1
- Initial package
