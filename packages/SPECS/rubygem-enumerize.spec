# Generated from enumerize-0.6.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name enumerize

Name: rubygem-%{gem_name}
Version: 0.6.1
Release: 1%{?dist}
Summary: Enumerated attributes with I18n and ActiveRecord/Mongoid support
Group: Development/Languages
License: MIT
URL: https://github.com/brainspec/enumerize
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(activesupport) >= 3.2
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: rubygem(minitest) 
BuildRequires: ruby >= 1.9.3
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Enumerated attributes with I18n and ActiveRecord/Mongoid support


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
#testrb -Ilib test/**/*.rb
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_spec}
%doc %{gem_instdir}/MIT-LICENSE
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Gemfile.rails4
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/test/

%changelog
* Fri Aug 09 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 0.6.1-1
- Initial package
