# Generated from puma-2.5.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name puma

Name: rubygem-%{gem_name}
Version: 2.5.0
Release: 1%{?dist}
Summary: Puma is a simple, fast, threaded, and highly concurrent HTTP 1.1 server for Ruby/Rack applications
Group: Development/Languages
License: BSD
URL: http://puma.io
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(rack) >= 1.1
Requires: rubygem(rack) < 2.0
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby-devel >= 1.8.7
Provides: rubygem(%{gem_name}) = %{version}

%description
Puma is a simple, fast, threaded, and highly concurrent HTTP 1.1 server for
Ruby/Rack applications. Puma is intended for use in both development and
production environments. In order to get the best throughput, it is highly
recommended that you use a  Ruby implementation with real threads like
Rubinius or JRuby.


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

mkdir -p %{buildroot}%{gem_extdir_mri}/lib/%{gem_name}/
mv %{buildroot}%{gem_libdir}/%{gem_name}/puma_http11.so %{buildroot}%{gem_extdir_mri}/lib/%{gem_name}/

rm -rf %{buildroot}%{gem_instdir}/ext/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
#testrb2 -Ilib test/
popd

%files
%dir %{gem_instdir}
%{_bindir}/puma
%{_bindir}/pumactl
%{gem_instdir}/bin
%{gem_libdir}
%{gem_extdir_mri}
%{gem_spec}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/COPYING
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/Manifest.txt
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/docs/config.md
%doc %{gem_instdir}/docs/nginx.md
%doc %{gem_instdir}/tools/jungle/README.md
%doc %{gem_instdir}/tools/jungle/init.d/README.md
%doc %{gem_instdir}/tools/jungle/upstart/README.md
%{gem_instdir}/tools/jungle/init.d/puma
%{gem_instdir}/tools/jungle/init.d/run-puma
%{gem_instdir}/tools/jungle/upstart/puma-manager.conf
%{gem_instdir}/tools/jungle/upstart/puma.conf
%{gem_instdir}/tools/trickletest.rb
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/test/
%{gem_instdir}/TODO


%changelog
* Sun Aug 11 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 2.5.0-1
- Initial package
