# Generated from backports-3.3.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name backports

Name: rubygem-%{gem_name}
Version: 3.3.2
Release: 1%{?dist}
Summary: Backports of Ruby features for older Ruby
Group: Development/Languages
License: MIT
URL: http://github.com/marcandre/backports
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildRequires: rubygem(minitest)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Essential backports that enable many of the nice features of Ruby 1.8.7 up to
2.0.0 for earlier versions.


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

%check
pushd .%{gem_instdir}
#testrb -Ilib test/
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_spec}
%doc %{gem_instdir}/LICENSE.txt
# Are these needed for tests?
%{gem_instdir}/tags/
%{gem_instdir}/set_version/
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/CHANGELOG.rdoc
%{gem_instdir}/Gemfile
%{gem_instdir}/Gemfile.lock
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/default.mspec
%{gem_instdir}/Rakefile
%{gem_instdir}/test/

%changelog
* Fri Sep 06 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 3.3.2-1
- Downgrade to 3.3.2

* Wed Aug 07 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 3.3.3-1
- Initial package
