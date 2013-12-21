# Generated from gitlab-gollum-lib-1.0.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name gitlab-gollum-lib

Name: rubygem-%{gem_name}
Version: 1.0.1
Release: 1%{?dist}
Summary: A simple, Git-powered wiki
Group: Development/Languages
License: MIT
URL: http://github.com/gollum/gollum-lib
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems)
Requires: rubygem(gitlab-grit) >= 2.5.1
Requires: rubygem(github-markup) >= 0.7.5
Requires: rubygem(github-markup) < 1.0.0
Requires: rubygem(github-markdown) => 0.5.3
Requires: rubygem(github-markdown) < 0.6
Requires: rubygem(pygments.rb) => 0.5.2
Requires: rubygem(pygments.rb) < 0.6
Requires: rubygem(sanitize) => 2.0.3
Requires: rubygem(sanitize) < 2.1
Requires: rubygem(nokogiri) => 1.5.9
Requires: rubygem(nokogiri) < 1.6
Requires: rubygem(stringex) => 2.0.3
Requires: rubygem(stringex) < 2.1
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 1.8.7
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
A simple, Git-powered wiki with a sweet API and local frontend.

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
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/licenses/licenses.txt
%{gem_spec}
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/HISTORY.md
%doc %{gem_instdir}/docs/sanitization.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/gollum-lib.gemspec

%changelog
* Sat Aug 10 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 1.0.1-1
- Initial package
