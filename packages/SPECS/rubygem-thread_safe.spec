# Generated from thread_safe-0.1.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name thread_safe

Name: rubygem-%{gem_name}
Version: 0.1.2
Release: 1%{?dist}
Summary: A collection of data structures and utilities to make thread-safe programming in Ruby easier
Group: Development/Languages
License: Apache-2.0
URL: https://github.com/headius/thread_safe
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(atomic) 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Thread-safe collections and utilities for Ruby


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
#testrb -Ilib test/*.rb
popd


%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_spec}
%doc %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/ext

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/examples/
%{gem_instdir}/test
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Thu Aug 08 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 0.1.2-1
- Initial package
