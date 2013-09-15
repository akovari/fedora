# Generated from omniauth-1.1.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name omniauth

Name: rubygem-%{gem_name}
Version: 1.1.4
Release: 2%{?dist}
Summary: A generalized Rack framework for multiple-provider authentication
Group: Development/Languages
License: MIT
URL: http://github.com/intridea/omniauth
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) >= 1.3.6
Requires: rubygem(hashie) >= 1.2
Requires: rubygem(hashie) < 3
Requires: rubygem(rack)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel >= 1.3.6
BuildRequires: ruby
BuildRequires: rubygem(hashie)
BuildRequires: rubygem(rack-test)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(simplecov)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
A generalized Rack framework for multiple-provider authentication.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}

%description doc
Documentation for %{name}

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

# Remove unneeded coveralls gem from test suite
sed -i '/[Cc]overalls/d' %{_builddir}/%{gem_name}-%{version}/spec/helper.rb

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
rspec spec/
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE.md
%doc %{gem_instdir}/README.md
%{gem_libdir}
%{gem_spec}
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/spec/

%changelog
* Tue Aug 27 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 1.1.4-2
- Remove set of noarch in -doc subpackage
- Move removal of coveralls gem to %prep
- Move README.md to main package

* Sun Jul 28 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 1.1.4-1
- Initial package
