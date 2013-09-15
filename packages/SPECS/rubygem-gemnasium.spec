# Generated from gemnasium-2.0.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name gemnasium

Name: rubygem-%{gem_name}
Version: 2.0.1
Release: 1%{?dist}
Summary: Safely upload your dependency files (Gemfile, Gemfile.lock, *.gemspec, package.json, npm-shrinkwrap.json) on gemnasium.com to track dependencies and get notified about updates and security advisories
Group: Development/Languages
License: MIT
URL: https://gemnasium.com/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
#BuildRequires: rubygem(rspec)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Safely upload your dependency files (Gemfile, Gemfile.lock, *.gemspec,
package.json, npm-shrinkwrap.json) on gemnasium.com to track dependencies and
get notified about updates and security advisories.


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
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
#rspec spec/
popd

%files
%dir %{gem_instdir}
%{_bindir}/gemnasium
%{gem_instdir}/bin
%{gem_libdir}
%doc %{gem_instdir}/LICENSE
%{gem_spec}
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/spec/
%{gem_instdir}/features/

%changelog
* Sat Aug 24 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 2.0.1-1
- Initial package
