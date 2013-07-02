# Generated from mini_portile-0.5.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name mini_portile

Name: rubygem-%{gem_name}
Version: 0.5.0
Release: 1%{?dist}
Summary: Simplistic port-like solution for developers
Group: Development/Languages
License: MIT
URL: http://github.com/luislavena/mini_portile
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) >= 1.3.5
BuildRequires: ruby(release)
BuildRequires: rubygems-devel >= 1.3.5
BuildRequires: ruby >= 1.8.7
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Simplistic port-like solution for developers. It provides a standard and
simplified way to compile against dependency libraries without messing up your
system.


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




%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{exclude} %{gem_instdir}/*.
%{gem_spec}
%doc %{gem_instdir}/LICENSE.txt

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/History.txt
%{gem_instdir}/Rakefile
%{gem_instdir}/examples/

%changelog
* Mon Jul 01 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 0.5.0-1
- Initial package
