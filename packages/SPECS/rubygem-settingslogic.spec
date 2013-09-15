# Generated from settingslogic-2.0.9.gem by gem2rpm -*- rpm-spec -*-
%global gem_name settingslogic

Name: rubygem-%{gem_name}
Version: 2.0.9
Release: 1%{?dist}
Summary: A simple and straightforward settings solution that uses an ERB enabled YAML file and a singleton design pattern
Group: Development/Languages
License: MIT
URL: http://github.com/binarylogic/settingslogic
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: rubygem(rspec) 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
A simple and straightforward settings solution that uses an ERB enabled YAML
file and a singleton design pattern.


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
rspec spec/
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
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Gemfile
%{gem_instdir}/Gemfile.lock
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/spec/

%changelog
* Sun Aug 11 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 2.0.9-1
- Initial package
