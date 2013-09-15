# Generated from omniauth-google-oauth2-0.2.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name omniauth-google-oauth2

Name: rubygem-%{gem_name}
Version: 0.2.0
Release: 1%{?dist}
Summary: A Google OAuth2 strategy for OmniAuth 1.x
Group: Development/Languages
License: MIT
URL: https://github.com/zquestz/omniauth-google-oauth2
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(omniauth) => 1.0
Requires: rubygem(omniauth) < 2
Requires: rubygem(omniauth-oauth2) 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildRequires: rubygem(rspec)
#BuildRequires: rubygem(sinatra)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
A Google OAuth2 strategy for OmniAuth 1.x


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

%check
pushd .%{gem_instdir}
#rspec spec/
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_spec}
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/omniauth-contrib.gemspec
%{gem_instdir}/spec/
%{gem_instdir}/examples/

%changelog
* Sat Aug 10 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 0.2.0-1
- Initial package
