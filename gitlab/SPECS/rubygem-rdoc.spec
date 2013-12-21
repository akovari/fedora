# Generated from rdoc-3.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rdoc

%global rubyabi 1.9.1

Summary: RDoc produces HTML and command-line documentation for Ruby projects
Name: rubygem-%{gem_name}
Version: 3.12.1
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2 and Ruby and MIT
URL: http://docs.seattlerb.org/rdoc/
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Requires: rubygem(json) => 1.4
Requires: rubygem(json) < 2
Requires: ruby(irb)
BuildRequires: rubygems-devel
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(json) => 1.4
BuildRequires: rubygem(json) < 2
BuildRequires: ruby(irb)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}
Obsoletes:  ruby-rdoc < 1.8.7.357-2

%description
RDoc produces HTML and command-line documentation for Ruby projects.  RDoc
includes the +rdoc+ and +ri+ tools for generating and displaying online
documentation.
See RDoc for a description of RDoc's markup and basic use.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
gem install --local --install-dir .%{gem_dir} \
            --bindir .%{_bindir} \
            --force %{SOURCE0}



%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x


%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE.rdoc
%doc %{gem_instdir}/LEGAL.rdoc
%exclude %{gem_instdir}/.*
%{_bindir}/rdoc
%{_bindir}/ri
%{gem_libdir}
%{gem_instdir}/bin
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/DEVELOPERS.rdoc
%doc %{gem_instdir}/History.rdoc
%doc %{gem_instdir}/Manifest.txt
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/CVE-2013-0256.rdoc
%doc %{gem_instdir}/RI.rdoc
%doc %{gem_instdir}/Rakefile
%doc %{gem_instdir}/TODO.rdoc
%doc %{gem_instdir}/test


%changelog
* Wed Feb 06 2013 Josef Stribny <jstribny@redhat.com> - 3.12.1-1
- Update to version 3.12.1

* Thu Sep 06 2012 Vít Ondruch <vondruch@redhat.com> - 3.12-5
- Fix the location of Ruby documentation (rhbz#854418).

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 02 2012 Vít Ondruch <vondruch@redhat.com> - 3.12-3
- Add missing obsolete (rhbz#809007).

* Mon Feb 13 2012 Vít Ondruch <vondruch@redhat.com> - 3.12-2
- Add missing IRB dependency.

* Tue Feb 07 2012 Vít Ondruch <vondruch@redhat.com> - 3.12-1
- Rebuilt for Ruby 1.9.3.
- Updated to RDoc 3.12.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Mo Morsi <mmorsi@redhat.com> - 3.8-2
- Fixes for fedora compliance

* Mon Jan 10 2011 mo morsi <mmorsi@redhat.com> - 3.8-1
- Initial package
