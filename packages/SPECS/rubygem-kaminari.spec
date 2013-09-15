# Generated from kaminari-0.14.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name kaminari

Name: rubygem-%{gem_name}
Version: 0.14.1
Release: 1%{?dist}
Summary: A pagination engine plugin for Rails 3 or other modern frameworks
Group: Development/Languages
License: MIT
URL: https://github.com/amatsuda/kaminari
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(activesupport) >= 3.0.0
Requires: rubygem(actionpack) >= 3.0.0
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(capybara)
BuildRequires: rubygem(rr)
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Kaminari is a Scope & Engine based, clean, powerful, agnostic, customizable
and sophisticated paginator for Rails 3


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
%{gem_spec}
%doc %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/config/
%{gem_instdir}/app/
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/CHANGELOG
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/spec/
%{gem_instdir}/gemfiles/
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Sat Aug 10 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 0.14.1-1
- Initial package
