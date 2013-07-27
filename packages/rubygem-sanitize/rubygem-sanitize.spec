# Generated from sanitize-2.0.6.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sanitize

Name: rubygem-%{gem_name}
Version: 2.0.6
Release: 1%{?dist}
Summary: Whitelist-based HTML sanitizer
Group: Development/Languages
License: MIT
URL: https://github.com/rgrove/sanitize/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) >= 1.2.0
Requires: rubygem(nokogiri) >= 1.4.4
BuildRequires: ruby(release)
BuildRequires: rubygems-devel >= 1.2.0
BuildRequires: ruby >= 1.9.2
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(nokogiri) >= 1.4.4
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Sanitize is a whitelist-based HTML sanitizer. Given a list of acceptable 
elements and attributes, Sanitize will remove all unacceptable HTML from 
a string.

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
testrb -Ilib test/test_sanitize.rb
rm -rf test
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/LICENSE
%{gem_spec}
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/HISTORY.md
%{gem_instdir}/test/

%changelog
* Sat Jul 27 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 2.0.6-1
- Initial package
