# Generated from seed-fu-2.2.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name seed-fu

Name: rubygem-%{gem_name}
Version: 2.2.0
Release: 1%{?dist}
Summary: Easily manage seed data in your Active Record application
Group: Development/Languages
License: MIT
URL: http://github.com/mbleigh/seed-fu
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(activerecord) => 3.1
Requires: rubygem(activerecord) < 4
Requires: rubygem(activesupport) => 3.1
Requires: rubygem(activesupport) < 4
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
#BuildRequires: rubygem(rspec)
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Seed Fu is an attempt to once and for all solve the problem of inserting and
maintaining seed data in a database. It uses a variety of techniques gathered
from various places around the web and combines them to create what is
hopefully the most robust seed data system around.


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
#rspec spec/
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/LICENSE
%{gem_spec}
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Sun Aug 11 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 2.2.0-1
- Initial package
