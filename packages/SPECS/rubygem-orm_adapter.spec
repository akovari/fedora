# Generated from orm_adapter-0.4.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name orm_adapter

Name: rubygem-%{gem_name}
Version: 0.4.0
Release: 2%{?dist}
Summary: Provides a single point of entry for using basic features of ruby ORMs
Group: Development/Languages
License: MIT
URL: http://github.com/ianwhite/orm_adapter
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) >= 1.3.6
BuildRequires: ruby(release)
BuildRequires: rubygems-devel >= 1.3.6
BuildRequires: rubygem(rspec) 
BuildRequires: rubygem(mongoid) 
BuildRequires: rubygem(activerecord) 
BuildRequires: rubygem(sqlite3) 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Provides a single point of entry for using basic features of ruby ORMs


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
## We are missing some tests because of missing packages:
## mongo_mapper, dm-core
rspec spec/
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_spec}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.rdoc
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.txt
%{gem_instdir}/spec/
%{gem_instdir}/Gemfile
%{gem_instdir}/Gemfile.lock.development
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/%{gem_name}.gemspec

%changelog
* Tue Aug 27 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 0.4.0-2
- Exclude Rakefile, gemspec
- Move README to main package

* Sun Jun 30 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 0.4.0-1
- Initial package
