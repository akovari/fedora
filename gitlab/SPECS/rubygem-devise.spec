# Generated from devise-2.2.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name devise

Name: rubygem-%{gem_name}
Version: 2.2.5
Release: 1%{?dist}
Summary: Flexible authentication solution for Rails with Warden
Group: Development/Languages
License: MIT
URL: http://github.com/plataformatec/devise
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(warden) => 1.2.1
Requires: rubygem(warden) < 1.3
Requires: rubygem(orm_adapter) => 0.1
Requires: rubygem(orm_adapter) < 1
Requires: rubygem(bcrypt-ruby) => 3.0
Requires: rubygem(bcrypt-ruby) < 4
Requires: rubygem(railties) => 3.1
Requires: rubygem(railties) < 4
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildRequires: rubygem(minitest) 
BuildRequires: rubygem(activerecord) 
BuildRequires: rubygem(rake) 
BuildRequires: rubygem(multi_json)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Flexible authentication solution for Rails with Warden


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
#find test -type f -name *_test.rb | xargs testrb -Ilib
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_spec}
%doc %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/app/*
%{gem_instdir}/config/locales/en.yml
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.rdoc
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/test/
%{gem_instdir}/Rakefile
%{gem_instdir}/Gemfile
%{gem_instdir}/Gemfile.lock
%{gem_instdir}/gemfiles/
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/%{gem_name}.png

%changelog
* Sun Jun 30 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 2.2.4-1
- Initial package
