# Generated from escape_utils-0.3.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name escape_utils

Name: rubygem-%{gem_name}
Version: 0.2.4
Release: 1%{?dist}
Summary: Faster string escaping routines for your web apps
Group: Development/Languages
License: MIT
URL: http://github.com/brianmario/escape_utils
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
BuildRequires: rubygem(rspec)
#BuildRequires: rubygem(minitest)
Provides: rubygem(%{gem_name}) = %{version}

%description
Faster string escaping routines for your ruby apps.
It supports HTML, URL, URI and Javascript escaping/unescaping.

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

mkdir -p %{buildroot}%{gem_extdir_mri}/lib/%{gem_name}/
# TODO: move the extensions
mv %{buildroot}%{gem_libdir}/%{gem_name}.so %{buildroot}%{gem_extdir_mri}/lib/%{gem_name}/%{gem_name}.so

# Remove the binary extension sources and build leftovers.
rm -rf %{buildroot}%{gem_instdir}/ext/

%check
pushd .%{gem_instdir}
# Remove bundler require
#sed -i '/bundler/d' test/helper.rb
#testrb -Ilib test/**/*.rb
#rspec spec/
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%{gem_extdir_mri}
%{gem_spec}
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/benchmark/
%{gem_instdir}/spec/


%changelog
* Fri Aug 09 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 0.3.2-1
- Initial package
