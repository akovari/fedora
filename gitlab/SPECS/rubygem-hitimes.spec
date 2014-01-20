# Generated from hitimes-1.2.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name hitimes

Name: rubygem-%{gem_name}
Version: 1.2.1
Release: 1%{?dist}
Summary: Hitimes is a fast, high resolution timer library for recording performance metrics.
Group: Development/Languages
License: ISC
URL: http://github.com/copiousfreetime/hitimes
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: rubygems
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(simplecov)
Provides: rubygem(%{gem_name}) = %{version}

%description
Hitimes is a fast, high resolution timer library for recording performance
metrics.  It uses the appropriate low method calls for each system to get the
highest granularity time increments possible.   It currently supports any of
the following systems: * any system with the POSIX call `clock_gettime()` *
Mac OS X * Windows * JRuby Using Hitimes can be faster than using a series of
`Time.new` calls, and it will have a much higher granularity. It is definitely
faster than using `Process.times`.

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

mkdir -p %{buildroot}%{gem_extdir_mri}/lib

mv %{buildroot}%{gem_instdir}/lib/hitimes/2.0/hitimes.so %{buildroot}%{gem_extdir_mri}/lib/

rm -rf %{buildroot}/%{gem_instdir}/ext/

%check
pushd ./%{gem_instdir}
rspec spec/
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/ext
%{gem_extdir_mri}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/HISTORY.md
%doc %{gem_instdir}/Manifest.txt
%doc %{gem_instdir}/README.md
%{gem_instdir}/spec/
%{gem_instdir}/tasks/
%{gem_instdir}/examples/
%{gem_instdir}/Rakefile

%changelog
* Mon Jan 20 2014 Achilleas Pipinellis <axilleaspi@ymail.com> - 1.2.1-1
- Initial package
