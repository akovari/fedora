# Generated from pkgwat-0.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name pkgwat

Name: rubygem-%{gem_name}
Version: 0.1.0
Release: 1%{?dist}
Summary: pkgwat checks your gems to against Fedora/EPEL
Group: Development/Languages
License: 
URL: https://github.com/daviddavis/pkgwat
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(nokogiri) = 1.5.5
Requires: rubygem(rake) 
Requires: rubygem(thor) 
Requires: rubygem(json) = 1.6.5
Requires: rubygem(sanitize) 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
pkgwat checks your Gemfile.lock to make sure all your gems
are packaged in Fedora/EPEL. Eventually we hope to support
Gemfiles and bundle list as well.


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

# remove some unecessary files
pushd .%{gem_instdir}
rm Gemfile
rm %{gem_name}.gemspec

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/




%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%changelog
* Thu Jun 27 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 0.1.0-1
- Initial package
