# Generated from compass-rails-1.0.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name compass-rails

Name: rubygem-%{gem_name}
Version: 1.0.3
Release: 1%{?dist}
Summary: Integrate Compass into Rails 2.3 and up
Group: Development/Languages
License: MIT
URL: https://github.com/Compass/compass-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(compass) >= 0.12.2
Requires: rubygem(compass) < 0.14
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Integrate Compass into Rails 2.3 and up.


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

popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/LICENSE
%{gem_spec}
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Appraisals
%{gem_instdir}/Gemfile
%{gem_instdir}/Guardfile
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/gemfiles/
%{gem_instdir}/test/
%exclude %{gem_instdir}/test/integrations/.gitkeep
%exclude %{gem_instdir}/test/units/.gitkeep
%exclude %{gem_instdir}/test/fixtures/.gitkeep

%changelog
* Wed Aug 07 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 1.0.3-1
- Initial package
