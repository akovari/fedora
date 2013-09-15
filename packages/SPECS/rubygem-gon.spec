# Generated from gon-4.1.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name gon

Name: rubygem-%{gem_name}
Version: 4.1.1
Release: 1%{?dist}
Summary: Get your Rails variables in your JS
Group: Development/Languages
License: MIT 
URL: https://github.com/gazay/gon
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(actionpack) >= 2.3.0
Requires: rubygem(json) 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
If you need to send some data to your js files and you don't want to do this
with long way trough views and parsing - use this force!


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
#rspec spec/
popd


%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/js/watch.js
%{gem_spec}
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/README_old.md
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/spec/
%{gem_instdir}/doc/
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Sat Aug 10 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 4.1.1-1
- Initial package
