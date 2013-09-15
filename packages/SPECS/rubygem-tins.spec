# Generated from tins-0.8.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name tins

Name: rubygem-%{gem_name}
Version: 0.8.4
Release: 1%{?dist}
Summary: Useful tools library in Ruby
Group: Development/Languages
License: MIT
URL: http://github.com/flori/tins
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(test-unit)
BuildRequires: rubygem(simplecov)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
All the stuff that isn't good/big enough for a real library.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

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
testrb2 -Ilib tests/
popd


%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/COPYING
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/tests/
%{gem_instdir}/VERSION
%exclude %{gem_instdir}/TODO

%changelog
* Tue Aug 13 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 0.8.3-1
- Initial package
