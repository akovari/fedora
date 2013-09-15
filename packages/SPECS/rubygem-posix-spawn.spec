# Generated from posix-spawn-0.3.6.gem by gem2rpm -*- rpm-spec -*-
%global gem_name posix-spawn

Name: rubygem-%{gem_name}
Version: 0.3.6
Release: 1%{?dist}
Summary: posix_spawnp(2) for ruby
Group: Development/Languages
License: MIT
URL: http://github.com/rtomayko/posix-spawn
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby-devel 
BuildRequires: rubygem(test-unit) 
Provides: rubygem(%{gem_name}) = %{version}

%description
posix-spawn uses posix_spawnp(2) for faster process spawning


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

mkdir -p %{buildroot}%{gem_extdir_mri}/lib/
mv %{buildroot}%{gem_libdir}/posix_spawn_ext.so %{buildroot}%{gem_extdir_mri}/lib/posix_spawn_ext.so

rm -rf %{buildroot}%{gem_instdir}/ext/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
#testrb2 -Ilib test/*.rb
popd

%files
%dir %{gem_instdir}
%{gem_instdir}/bin
%{_bindir}/posix-spawn-benchmark
%{gem_libdir}
%{gem_extdir_mri}
%{gem_spec}
%doc %{gem_instdir}/COPYING
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/HACKING
%doc %{gem_instdir}/README.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/test/
%{gem_instdir}/TODO

%changelog
* Sun Aug 11 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 0.3.6-1
- Initial package
