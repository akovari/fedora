# Generated from omniauth-github-1.1.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name omniauth-github

Name: rubygem-%{gem_name}
Version: 1.1.1
Release: 1%{?dist}
Summary: Official OmniAuth strategy for GitHub
Group: Development/Languages
License: MIT
URL: https://github.com/intridea/omniauth-github
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(omniauth) => 1.0
Requires: rubygem(omniauth) < 2
Requires: rubygem(omniauth-oauth2) => 1.1
Requires: rubygem(omniauth-oauth2) < 2
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
#BuildRequires: rubygem(rspec)
#BuildRequires: rubygem(webmock)
#BuildRequires: rubygem(omniauth-oauth2)
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Official OmniAuth strategy for GitHub.


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
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/Guardfile
%{gem_instdir}/spec/
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Sat Aug 10 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 1.1.1-1
- Initial package
