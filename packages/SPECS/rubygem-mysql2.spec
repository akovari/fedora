# Generated from mysql2-0.3.11.gem by gem2rpm -*- rpm-spec -*-
%global gem_name mysql2

Name: rubygem-%{gem_name}
Version: 0.3.13
Release: 1%{?dist}
Summary: A simple, fast Mysql library for Ruby, binding to libmysql
Group: Development/Languages
License: MIT
URL: http://github.com/brianmario/mysql2
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems)
Requires: mariadb-libs
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
BuildRequires: rubygem(rspec)
BuildRequires: mariadb-devel
BuildRequires: mariadb-server
Provides: rubygem(%{gem_name}) = %{version}

%description
The Mysql2 gem is meant to serve the extremely common use-case of
connecting, querying and iterating on results. Some database libraries
out there serve as direct 1:1 mappings of the already complex C API\'s
available. This one is not.


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
mv %{buildroot}%{gem_libdir}/%{gem_name}/%{gem_name}.so %{buildroot}%{gem_extdir_mri}/lib/%{gem_name}/

rm -rf %{buildroot}%{gem_instdir}/ext/

%check
# We can't run the tests because they require a mysql instance. That's
# a bit much to require for builds. The following invocation is documentation
#systemctl start mysqld.service
#rspec -I%%{buildroot}%%{gem_extdir_mri}/lib/ spec


%files
%dir %{gem_instdir}
%doc %{gem_instdir}/MIT-LICENSE
%{gem_extdir_mri}
%{gem_libdir}
%{gem_spec}
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/examples/
%{gem_instdir}/support/
%{gem_instdir}/spec/


%changelog
* Sun Jun 16 2013 Alexander Chernyakhovsky <achernya@mit.edu> - 0.3.11-1
- Initial package
