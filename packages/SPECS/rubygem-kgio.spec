%global gem_name kgio

%global rubyabi 1.9.1

%if 0%{?fedora} >= 17
  %global rubyabi 1.9.1
%endif

%if 0%{?fedora} >= 19
  %global rubyabi 2.0.0
%endif

Summary:       Kinder, gentler I/O for Ruby
Name:          rubygem-%{gem_name}
Version:       2.8.0
Release:       4%{?dist}
Group:         Development/Tools
License:       LGPLv2 or LGPLv3
# LICENSE file defines the licencing aspects of kgiox.
# No license info in source files.
URL:           http://bogomips.org/kgio
Source0:       http://rubygems.org/downloads/%{gem_name}-%{version}.gem
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%if 0%{?fedora} >= 19
Requires:       ruby(release)
%{?rubygems_default_filter}
%endif

%if 0%{?fedora} >= 17 && 0%{?fedora} < 19
Requires:      ruby(abi) = %{rubyabi}
Requires:      ruby(rubygems)
%endif

BuildRequires: ruby-devel
BuildRequires: ruby-irb
BuildRequires: rubygems-devel
BuildRequires: rubygem(minitest)
Provides:      rubygem(%{gem_name}) = %{version}
ExcludeArch:   ppc ppc64

%description
kgio provides non-blocking I/O methods for Ruby without raising
exceptions on EAGAIN and EINPROGRESS.  It is intended for use with the
Unicorn and Rainbows! Rack servers, but may be used by other
applications (that run on Unix-like platforms).

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}

%description doc
Documentation for %{name}

%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
gem install \
        -V \
        --local \
        --install-dir .%{gem_dir} \
	--force \
	--rdoc \
	%{SOURCE0}

# Adjusting minor permissions
chmod a+r .%{gem_instdir}/ChangeLog
chmod a+r .%{gem_instdir}/NEWS

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
mkdir -p %{buildroot}%{gem_extdir}/lib
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

# Remove the binary extension sources and build leftovers.
rm -f %{buildroot}%{gem_instdir}/.document
rm -f %{buildroot}%{gem_instdir}/.gitignore
rm -f %{buildroot}%{gem_instdir}/.manifest
rm -f %{buildroot}%{gem_instdir}/.wrongdoc.yml
rm -f %{buildroot}%{gem_instdir}/pkg.mk
rm -f %{buildroot}%{gem_instdir}/setup.rb
rm -f %{buildroot}/%{gem_instdir}/kgio.gemspec
rm -f %{buildroot}/%{gem_instdir}/GNUmakefile
rm -f %{buildroot}/%{gem_instdir}/GIT-VERSION-FILE
rm -f %{buildroot}/%{gem_instdir}/GIT-VERSION-GEN
rm -rf %{buildroot}%{gem_instdir}/.yardoc
rm -rf %{buildroot}%{gem_instdir}/ext

# If there are C extensions, mv them to the extdir.
# You must replace REQUIRE_PATHS according to your gem specifics.
%if 0%{?fedora} >= 17 && 0%{?fedora} < 19
install -d -m0755 %{buildroot}%{gem_extdir}
mv %{buildroot}%{gem_instdir}/lib/kgio_ext.so %{buildroot}%{gem_extdir}/lib/
%endif

%if 0%{?fedora} >= 19
install -d m0755 %{buildroot}%{gem_extdir_mri}/lib
mv %{buildroot}%{gem_instdir}/lib/kgio_ext.so %{buildroot}%{gem_extdir_mri}/lib/
%endif

%check
cd %{buildroot}%{gem_instdir}
RUBYOPT="-Ilib -I%{buildroot}%{gem_extdir}/lib -Itest" testrb test/test_*

%clean
rm -rf %{buildroot}

%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{gem_instdir}/TODO
%doc %{gem_instdir}/LATEST
%doc %{gem_instdir}/Rakefile
%doc %{gem_instdir}/ISSUES
%doc %{gem_instdir}/HACKING
%doc %{gem_instdir}/test

%files
%if 0%{?fedora} >= 19
%{gem_extdir_mri}
#%%{gem_extdir_mri} 	%%{_libdir}/gems/ruby/%%{gem_name}-%%{version}
%endif

%if 0%{?fedora} >= 17 && 0%{?fedora} < 19
%{gem_extdir}
#%%{gem_extdir} 	%%{_libdir}/gems/exts/%%{gem_name}-%%{version}
%endif

%dir %{gem_instdir}/lib
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/COPYING
%doc %{gem_instdir}/README
%doc %{gem_instdir}/NEWS
%doc %{gem_instdir}/ChangeLog
%{gem_cache}
%{gem_spec}
%{gem_instdir}/lib/kgio.rb

%changelog
* Fri Sep 06 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 2.8.0-4
- Add binary filter macro

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 23 2013 Guillermo Gómez <guillermo.gomez@gmail.com> - 2.8.0-2
- Fixes for Ruby 2.0.0 packaging guidelines

* Sun Feb 10 2013 Guillermo Gómez <guillermo.gomez@gmail.com> - 2.8.0-1
- Update version 2.8.0

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 23 2012 Guillermo Gómez <guillermo.gomez@gmail.com> - 2.7.3-1
- Update version 2.7.3

* Sun Feb 12 2012 Guillermo Gómez <guillermo.gomez@gmail.com> - 2.7.0-5
- Proper use of new macros for Ruby 1.9 packaging
- irb added as build require

* Sat Jan 07 2012 Guillermo Gómez <guillermo.gomez@gmail.com> - 2.7.0-4
- Requires fixed for Ruby 1.9

* Sun Jan 01 2012 Guillermo Gómez <guillermo.gomez@gmail.com> - 2.7.0-3
- Path to kgio_ext.so at spec file check section fixed
- Moved patching test file to install section
- Unused macro removed from spec file

* Sat Dec 31 2011 Guillermo Gómez <guillermo.gomez@gmail.com> - 2.7.0-2
- For now rdoc-generated files arch-dependent
- defattr at the beginning of files remove
- README, NEWS, ChangeLog location fixed
- Test suite enabled during build time
- kgio_ext.so placed under ruby_sitearch dir

* Fri Dec 30 2011 Guillermo <guillermo.gomez@gmail.com> - 2.7.0-1
- Initial package
