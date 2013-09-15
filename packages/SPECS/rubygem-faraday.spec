# Generated from faraday-0.8.7.gem by gem2rpm -*- rpm-spec -*-
%global gem_name faraday

Name: rubygem-%{gem_name}
Version: 0.8.8
Release: 1%{?dist}
Summary: HTTP/REST API client library
Group: Development/Languages
License: MIT
URL: https://github.com/lostisland/faraday
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) >= 1.3.6
Requires: rubygem(multipart-post) => 1.1
Requires: rubygem(multipart-post) < 2
BuildRequires: ruby(release)
BuildRequires: wget
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(multipart-post) => 1.1
BuildRequires: rubygem(multipart-post) < 2
BuildRequires: rubygems-devel >= 1.3.6
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
HTTP/REST API client library

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

%check
pushd .%{gem_instdir}
testrb -Ilib test/*_test.rb
popd


%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_spec}
%doc %{gem_instdir}/LICENSE.md
%doc %{gem_instdir}/README.md
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/script
%{gem_instdir}/test
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile

%changelog
* Sun Aug 04 2013 Anuj More - 0.8.8-1
- From 0.8.7 to 0.8.8

* Tue May 14 2013 Anuj More - 0.8.7-1
- Initial package
