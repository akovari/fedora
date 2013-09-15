# Generated from grape-entity-0.3.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name grape-entity

Name: rubygem-%{gem_name}
Version: 0.3.0
Release: 1%{?dist}
Summary: A simple facade for managing the relationship between your model and API
Group: Development/Languages
License: MIT
URL: https://github.com/intridea/grape-entity
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(activesupport) 
Requires: rubygem(multi_json) >= 1.3.2
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildRequires: rubygem(grape)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(pry)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Extracted from Grape, A Ruby framework for rapid API development with great
conventions.


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
# Remove bundler
#sed -i '/[Bb]undler/d' spec/spec_helper.rb
#rspec spec/
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/LICENSE
%{gem_spec}
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.markdown
%doc %{gem_instdir}/README.markdown
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/Guardfile
%{gem_instdir}/spec/
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Sat Aug 10 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 0.3.0-1
- Initial package
