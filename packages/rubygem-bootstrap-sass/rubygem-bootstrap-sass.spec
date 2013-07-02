# Generated from bootstrap-sass-2.3.2.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name bootstrap-sass

Name: rubygem-%{gem_name}
Version: 2.3.2.0
Release: 1%{?dist}
Summary: Twitter's Bootstrap, converted to Sass and ready to drop into Rails or Compass
Group: Development/Languages
License: Apache 2.0
URL: http://github.com/thomas-mcdonald/bootstrap-sass
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/thomas-mcdonald/bootstrap-sass.git && cd bootstrap-sass
# git checkout v2.3.2.0
# tar -czf ../rubygem-bootstrap-sass-2.3.2.0-test.tgz test/
Source1: %{name}-%{version}-test.tgz
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(sass) => 3.2
Requires: rubygem(sass) < 4
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(sass)
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Twitter's Bootstrap, converted to Sass and ready to drop into Rails or Compass

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

tar -xvzf %{SOURCE1} 

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
cp -pr test .%{gem_instdir}
testrb -Ilib test/*_test.rb
rm -rf test/
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE
%{gem_instdir}/vendor/
%{gem_instdir}/templates/

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Sun Jun 16 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 2.3.2.0-1
- Initial package
