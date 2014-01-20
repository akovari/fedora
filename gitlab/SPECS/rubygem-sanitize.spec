# Generated from sanitize-2.0.6.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sanitize

Name: rubygem-%{gem_name}
Version: 2.1.0
Release: 1%{?dist}
Summary: Whitelist-based HTML sanitizer
Group: Development/Languages
License: MIT
URL: https://github.com/rgrove/sanitize/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: rubygems
Requires: rubygem(nokogiri) >= 1.4.4
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(nokogiri)
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

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
testrb -Ilib test/test_sanitize.rb
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/LICENSE
%{gem_spec}
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/HISTORY.md
%{gem_instdir}/test/

%changelog
* Mon Jan 20 2014 Achilleas Pipinellis <axilleaspi@ymail.com> - 2.1.0-1
- Bump version
- Clean up spec

* Sat Jul 27 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 2.0.6-2
- Tests don't need to be removed
- Fix BR nokogiri to match upstream gemspec

* Sat Jul 27 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 2.0.6-1
- Initial package
