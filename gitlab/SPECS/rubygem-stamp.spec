# Generated from stamp-0.5.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name stamp

Name: rubygem-%{gem_name}
Version: 0.5.0
Release: 1%{?dist}
Summary: Date and time formatting for humans
Group: Development/Languages
License: MIT
URL: https://github.com/jeremyw/stamp
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(cucumber)
BuildRequires: rubygem(minitest)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Format dates and times based on human-friendly examples, not arcane strftime
directives.


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
sed -i '1,8d' features/support/env.rb
cucumber features/
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/LICENSE.txt
%{gem_spec}
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/features/
%{gem_instdir}/cucumber.yml

%changelog
* Tue Aug 13 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 0.5.0-1
- Initial package
