# Generated from charlock_holmes-0.6.9.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name charlock_holmes

Name: rubygem-%{gem_name}
Version: 0.6.9.4
Release: 4%{?dist}
Summary: Character encoding detection, brought to you by ICU
Group: Development/Languages
License: MIT
URL: http://github.com/brianmario/charlock_holmes
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
BuildRequires: libicu-devel
BuildRequires: rubygem(minitest)
Provides: rubygem(%{gem_name}) = %{version}

# The Python code in the tests subdirectory references /usr/bin/env.
# Filter this from RPM's autorequires.
%global __requires_exclude ^/usr/bin/env$

# Filter .so files
%{?rubygems_default_filter}

%description
Character encoding detecting library for Ruby using ICU

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

# Remove unecessary bundler dependency
sed -i '/bundler/d' test/helper.rb

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

mkdir -p %{buildroot}%{gem_extdir_mri}/lib/%{gem_name}
mv %{buildroot}%{gem_libdir}/%{gem_name}/%{gem_name}.so %{buildroot}%{gem_extdir_mri}/lib/%{gem_name}/

# Remove the binary extension sources and build leftovers.
rm -rf %{buildroot}/%{gem_instdir}/ext/

# Fix permission
chmod +x %{buildroot}/%{gem_instdir}/test/fixtures/laholator.py

%check
pushd .%{gem_instdir}
# Set locale to UTF due to failing tests in mock
# https://github.com/brianmario/charlock_holmes/issues/39
LANG=en_US.utf8
testrb -Ilib test/*.rb
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_extdir_mri}
%{gem_spec}
%doc %{gem_instdir}/MIT-LICENSE
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Gemfile.lock
%{gem_instdir}/Rakefile
%{gem_instdir}/benchmark/
%{gem_instdir}/test/
%{gem_instdir}/%{gem_name}.gemspec


%changelog
* Fri Sep 06 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 0.6.9.4-4
- Add macro about filtering .so file

* Wed Aug 07 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 0.6.9.4-3
- Filter /usr/bin/env from RPM's autorequires
- Removed extra newline from description

* Sun Aug 04 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 0.6.9.4-2
- Move bundler removal to %prep
- Include github issue of failing tests

* Mon Jul 22 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 0.6.9.4-1
- Initial package
