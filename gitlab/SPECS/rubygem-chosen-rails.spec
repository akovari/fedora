# Generated from chosen-rails-1.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name chosen-rails

Name: rubygem-%{gem_name}
Version: 1.0.0
Release: 1%{?dist}
Summary: Integrate Chosen javascript library with Rails asset pipeline
Group: Development/Languages
License: MIT
URL: https://github.com/tsechingho/chosen-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(railties) >= 3.0
Requires: rubygem(coffee-rails) >= 3.2
Requires: rubygem(sass-rails) >= 3.2
Requires: rubygem(compass-rails) >= 1.0
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Chosen is a javascript library of select box enhancer for jQuery and Protoype.
This gem integrates Chosen with Rails asset pipeline for easy of use.


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
%{gem_spec}
%doc %{gem_instdir}/LICENSE
%{gem_instdir}/vendor//
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Wed Aug 07 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 1.0.0-1
- Initial package
