# Generated from github-markdown-0.5.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name github-markdown

Name: rubygem-%{gem_name}
Version: 0.5.3
Release: 1%{?dist}
Summary: The Markdown parser for GitHub.com
Group: Development/Languages
License: MIT
URL: http://github.github.com/github-flavored-markdown/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby-devel 
Provides: rubygem(%{gem_name}) = %{version}

%description
Self-contained Markdown parser for GitHub, with all our custom extensions


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

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{gem_instdir}/bin/gfm \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

mkdir -p %{buildroot}%{gem_extdir_mri}/lib/github/
mv %{buildroot}%{gem_libdir}/github/markdown.so %{buildroot}%{gem_extdir_mri}/lib/github/markdown.so

rm -rf %{buildroot}%{gem_instdir}/ext/

%check
pushd .%{gem_instdir}
#testrb -Ilib test/gfm_test.rb
popd

%files
%dir %{gem_instdir}
%{_bindir}/gfm
%{gem_instdir}/bin
%{gem_libdir}
%{gem_extdir_mri}
%{gem_spec}
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/test/

%changelog
* Fri Aug 09 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 0.5.3-1
- Initial package
