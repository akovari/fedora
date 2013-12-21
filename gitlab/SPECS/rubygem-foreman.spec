# Generated from foreman-0.63.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name foreman

Name: rubygem-%{gem_name}
Version: 0.63.0
Release: 1%{?dist}
Summary: Process manager for applications with multiple components
Group: Development/Languages
License: MIT
URL: http://github.com/ddollar/foreman
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(thor) >= 0.13.6
Requires: rubygem(dotenv) >= 0.7
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildRequires: rubygem(timecop) 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Process manager for applications with multiple components


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


mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

mkdir -p %{buildroot}%{_mandir}/man1
cp -a %{buildroot}%{gem_instdir}/man/%{gem_name}.1 %{buildroot}%{_mandir}/man1/

%check
pushd .%{gem_instdir}
#rspec spec/
popd

%files
%dir %{gem_instdir}
%{_bindir}/foreman
%{gem_instdir}/bin
%{gem_libdir}
%{gem_spec}
%{gem_instdir}/data/
%doc %{_mandir}/man1/*
%exclude %{gem_cache}
%exclude %{gem_instdir}/man

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/spec/

%changelog
* Fri Aug 09 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 0.63.0-1
- Initial package
