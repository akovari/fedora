# Generated from select2-rails-3.4.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name select2-rails

Name: rubygem-%{gem_name}
Version: 3.4.3
Release: 1%{?dist}
Summary: Integrate Select2 javascript library with Rails asset pipeline
Group: Development/Languages
License: 
URL: https://github.com/argerim/select2-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(thor) => 0.14
Requires: rubygem(thor) < 1
Requires: rubygem(sass-rails) 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Select2 is a jQuery based replacement for select boxes. It supports searching,
remote data sets, and infinite scrolling of results. This gem integrates
Select2 with Rails asset pipeline for easy of use.


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
* Mon Jul 08 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 3.4.3-1
- Initial package
