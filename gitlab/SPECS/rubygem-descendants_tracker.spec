# Generated from descendants_tracker-0.0.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name descendants_tracker

Name: rubygem-%{gem_name}
Version: 0.0.1
Release: 1%{?dist}
Summary: Module that adds descendant tracking to a class
Group: Development/Languages
License: MIT
URL: https://github.com/dkubb/descendants_tracker
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildRequires: rubygem(rspec) 
BuildRequires: rubygem(simplecov) 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Module that adds descendant tracking to a class


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
# Remove coveralls
#sed -i '/[Cc]overalls/d' spec/spec_helper.rb
#rspec spec/
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_spec}
%doc %{gem_instdir}/LICENSE
%{gem_instdir}/config/
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/TODO

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/Guardfile
%{gem_instdir}/spec/
%{gem_instdir}/tasks/
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Thu Aug 08 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 0.0.1-1
- Initial package
