# Generated from unicorn-4.6.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name unicorn

Name: rubygem-%{gem_name}
Version: 4.6.3
Release: 2%{?dist}
Summary: Rack HTTP server for fast clients and Unix
Group: Development/Languages
License: GPLv2 and GPLv3 and Ruby 1.8
URL: http://unicorn.bogomips.org/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems)
Requires: rubygem(rack)
Requires: rubygem(kgio) => 2.6
Requires: rubygem(kgio) < 3
Requires: rubygem(raindrops) => 0.7
Requires: rubygem(raindrops) < 1
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(raindrops) => 0.7
BuildRequires: rubygem(kgio) => 2.6
BuildRequires: rubygem(rack)
BuildRequires: rubygem(minitest)
BuildRequires: ruby-devel
Provides: rubygem(%{gem_name}) = %{version}

# Many scripts reference /usr/bin/env.
# Filter this from RPM's autorequires.
%global __requires_exclude ^/usr/bin/env$

%description
\Unicorn is an HTTP server for Rack applications designed to only serve
fast clients on low-latency, high-bandwidth connections and take
advantage of features in Unix/Unix-like kernels.  Slow clients should
only be served by placing a reverse proxy capable of fully buffering
both the the request and response in between \Unicorn and slow clients.

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

# Fix wrong shebang
grep -rl /this/will/be/overwritten/or/wrapped/anyways/do/not/worry/ruby \
        %{_builddir}/%{gem_name}-%{version}/bin/unicorn | \
        xargs sed -i -e 's|/this/will/be/overwritten/or/wrapped/anyways/do/not/worry/ruby|/usr/bin/ruby|'

grep -rl /this/will/be/overwritten/or/wrapped/anyways/do/not/worry/ruby \
        %{_builddir}/%{gem_name}-%{version}/bin/unicorn_rails | \
        xargs sed -i -e 's|/this/will/be/overwritten/or/wrapped/anyways/do/not/worry/ruby|/usr/bin/ruby|'


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

mkdir -p %{buildroot}%{gem_extdir_mri}/lib
mv %{buildroot}%{gem_libdir}/unicorn_http.so %{buildroot}%{gem_extdir_mri}/lib/unicorn_http.so

rm -rf %{buildroot}%{gem_instdir}/ext/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

mkdir -p %{buildroot}%{_mandir}
cp -a %{buildroot}%{gem_instdir}/man/* %{buildroot}%{_mandir}/

%check
pushd .%{gem_instdir}
#testrb2 -Ilib test/
popd

%files
%dir %{gem_instdir}
%{_bindir}/unicorn
%{_bindir}/unicorn_rails
%{gem_instdir}/bin
%{gem_libdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/COPYING
%doc %{gem_instdir}/man/man1/
%doc %{_mandir}/man1/
%{gem_spec}
%{gem_extdir_mri}
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/FAQ
%doc %{gem_instdir}/README
%doc %{gem_instdir}/ChangeLog
%doc %{gem_instdir}/TUNING
%doc %{gem_instdir}/PHILOSOPHY
%doc %{gem_instdir}/HACKING
%doc %{gem_instdir}/DESIGN
%doc %{gem_instdir}/SIGNALS
%doc %{gem_instdir}/KNOWN_ISSUES
%doc %{gem_instdir}/TODO
%doc %{gem_instdir}/NEWS
%doc %{gem_instdir}/LATEST
%doc %{gem_instdir}/ISSUES
%doc %{gem_instdir}/Sandbox
%doc %{gem_instdir}/Links
%doc %{gem_instdir}/Application_Timeouts
%doc %{gem_instdir}/Documentation/
%{gem_instdir}/CONTRIBUTORS
%{gem_instdir}/examples/
%{gem_instdir}/test/
%{gem_instdir}/t/
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/GIT-VERSION-FILE
%{gem_instdir}/GIT-VERSION-GEN
%{gem_instdir}/GNUmakefile
%{gem_instdir}/local.mk.sample
%{gem_instdir}/script/isolate_for_tests
%{gem_instdir}/setup.rb
%exclude %{gem_instdir}/Documentation/.gitignore
%exclude %{gem_instdir}/t/.gitignore

%changelog
* Wed Aug 28 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 4.6.3-2
- Fix wrong shebang

* Wed Aug 14 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 4.6.3-1
- Initial package
