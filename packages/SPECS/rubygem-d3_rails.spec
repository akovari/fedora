# Generated from d3_rails-3.2.8.gem by gem2rpm -*- rpm-spec -*-
%global gem_name d3_rails

Name: rubygem-%{gem_name}
Version: 3.3.2
Release: 1%{?dist}
Summary: D3 automated install for Rails 3.1+
Group: Development/Languages
License: MIT and BSD
URL: https://github.com/logical42/d3_rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(railties) >= 3.1.0
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Gem installation of javascript framework for data visualization, D3


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

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/MIT_LICENSE
%doc %{gem_instdir}/LICENSE
%{gem_instdir}/app/
%{gem_spec}
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/app/assets/stylesheets/.gitkeep

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Fri Aug 30 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 3.3.2-1
- Update to 3.3.2

* Thu Aug 08 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 3.2.8-1
- Initial package
