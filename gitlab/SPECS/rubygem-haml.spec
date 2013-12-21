# Generated from haml-2.2.14.gem by gem2rpm -*- rpm-spec -*-
%global gem_name haml

Summary: An elegant, structured XHTML/XML templating engine
Name: rubygem-%{gem_name}
Version: 4.0.3
Release: 1%{?dist}
Group: Development/Languages
License: MIT and WTFPL
URL: http://haml-lang.com/
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(rubygems)
Requires: ruby(release)
Requires: rubygem(tilt) >= 0
BuildRequires: rubygems-devel
BuildRequires: rubygem(minitest)

BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Haml (HTML Abstraction Markup Language) is a layer on top of XHTML or XML
that's designed to express the structure of XHTML or XML documents in a
non-repetitive, elegant, easy way, using indentation rather than closing
tags and allowing Ruby to be embedded with ease.
It was originally envisioned as a plugin for Ruby on Rails, but it can
function as a stand-alone templating engine.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -q -c -T
%gem_install -n %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Fix wrong permissions
for file in `find %{buildroot}%{gem_instdir}/lib/haml/ -type f -perm /a+x`; do
  chmod 644 $file
done

%check
pushd .%{gem_instdir}
testrb -Ilib test/*_test.rb
popd

%files
%{_bindir}/haml
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/bin
%doc %{gem_instdir}/MIT-LICENSE
%{gem_spec}
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/FAQ.md
%doc %{gem_instdir}/REFERENCE.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Thu Sep 05 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 4.0.3-1
- Update to 4.0.3

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 12 2013 Vít Ondruch <vondruch@redhat.com> - 3.1.7-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 13 2012 Mo Morsi <mmorsi@redhat.com> - 3.1.7-1
- updated to latest upstream release

* Fri Jul 27 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.1.6-1
- Updated to Haml 3.1.6.
- Removed patch that is included in this upstream release.
- Introduced -doc subpackage.
- Simplified the test running.
- Adjusted Requires accordingly.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 01 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.1.2-5
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 20 2011 Mo Morsi <mmorsi@redhat.com> - 3.1.2-3
- remove fssm dependency as upstream project no longer bundles it
  (sass, which is vendored by haml upstream, still depends on it)

* Fri Jul 22 2011 Chris Lalancette <clalance@redhat.com> - 3.1.2-2
- Fix up the sass includes

* Mon Jul 11 2011 Mo Morsi <mmorsi@redhat.com> - 3.1.2-1
- updated to latest upstream release

* Tue Mar 29 2011 Mo Morsi <mmorsi@redhat.com> - 3.0.25-1
- updated to latest upstream release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Aug 26 2010 Matthew Kent <mkent@magoazul.com> - 3.0.17-1
- New upstream version.
- Include VERSION and VERSION_NAME in main package (#627454).
- Exclude vendored copy of fssm.

* Thu Aug 12 2010 Matthew Kent <mkent@magoazul.com> - 3.0.15-2
- New BR on rubygem-erubis and ruby_parser.

* Wed Jul 28 2010 Matthew Kent <mkent@magoazul.com> - 3.0.15-1
- New upstream version.
- New dependencies on yard/maruku.

* Tue May 4 2010 Matthew Kent <mkent@magoazul.com> - 2.2.24-1
- New upstream version - minor bugfixes and improvements.
- Drop unused sitelib macro.
- No backup files to cleanup now.

* Mon Jan 04 2010 Michal Babej <mbabej@redhat.com> - 2.2.20-1
- update to new upstream release

* Mon Jan 04 2010 Michal Babej <mbabej@redhat.com> - 2.2.16-1
- update to new upstream release
- get rid of test_files macro
- add shebang/permission handling from Jeroen van Meeuwen

* Fri Dec 04 2009 Michal Babej <mbabej@redhat.com> - 2.2.15-2
- change %%define to %%global
- change license to "MIT and WTFPL" (test/haml/spec/README.md)
- add Requires on hpricot for html2haml
- change %%gem_dir to %%gem_instdir where appropriate

* Wed Dec 02 2009 Michal Babej <mbabej@redhat.com> - 2.2.15-1
- Update to new upstream release
- URL changed by upstream

* Wed Dec 02 2009 Michal Babej <mbabej@redhat.com> - 2.2.14-1
- Initial package
