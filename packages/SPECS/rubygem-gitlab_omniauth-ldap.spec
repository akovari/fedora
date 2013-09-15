# Generated from gitlab_omniauth-ldap-1.0.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name gitlab_omniauth-ldap

Name: rubygem-%{gem_name}
Version: 1.0.3
Release: 1%{?dist}
Summary: A LDAP strategy for OmniAuth
Group: Development/Languages
License: MIT
URL: https://github.com/gitlabhq/omniauth-ldap
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems)
Requires: rubygem(omniauth) => 1.0
Requires: rubygem(omniauth) < 2
Requires: rubygem(net-ldap) => 0.3.1
Requires: rubygem(net-ldap) < 0.4
Requires: rubygem(pyu-ruby-sasl) => 0.0.3.1
Requires: rubygem(pyu-ruby-sasl) < 0.0.4
Requires: rubygem(rubyntlm) => 0.1.1
Requires: rubygem(rubyntlm) < 0.2
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(omniauth)
BuildRequires: rubygem(net-ldap)
BuildRequires: rubygem(rack-test)
BuildRequires: rubygem(rubyntlm)
BuildRequires: rubygem(pyu-ruby-sasl)
BuildRequires: rubygem(rspec)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
A LDAP strategy for OmniAuth.


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
rspec spec/
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
%{gem_instdir}/Gemfile.lock
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/spec/
%{gem_instdir}/Guardfile

%changelog
* Wed Aug 21 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 1.0.3-1
- Initial package
