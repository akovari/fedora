# Generated from grape-0.5.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name grape

Name: rubygem-%{gem_name}
Version: 0.5.0
Release: 1%{?dist}
Summary: A simple Ruby framework for building REST-like APIs
Group: Development/Languages
License: MIT
URL: https://github.com/intridea/grape
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(rack) >= 1.3.0
Requires: rubygem(rack-mount) 
Requires: rubygem(rack-accept) 
Requires: rubygem(activesupport) 
Requires: rubygem(multi_json) >= 1.3.2
Requires: rubygem(multi_xml) >= 0.5.2
Requires: rubygem(hashie) >= 1.2.0
Requires: rubygem(virtus) 
Requires: rubygem(builder) 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
A Ruby framework for rapid API development with great conventions.


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

%changelog
* Mon Jul 08 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 0.5.0-1
- Initial package
