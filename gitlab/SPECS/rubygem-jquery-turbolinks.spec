# Generated from jquery-turbolinks-1.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name jquery-turbolinks

Name: rubygem-%{gem_name}
Version: 2.0.1
Release: 1%{?dist}
Summary: jQuery plugin for drop-in fix binded events problem caused by Turbolinks
Group: Development/Languages
License: MIT
URL: https://github.com/kossnocorp/jquery.turbolinks
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems)
Requires: rubygem(railties) >= 3.1.0
Requires: rubygem(turbolinks)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
jQuery plugin for drop-in fix binded events problem caused by Turbolinks


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

popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/LICENSE.md
%{gem_spec}
%{gem_instdir}/vendor/
%{gem_instdir}/src/
%{gem_instdir}/package.json
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/NOTES.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/Guardfile
%{gem_instdir}/spec/
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Thu Sep 05 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 2.0.1-1
- Update to 2.0.1

* Sat Aug 10 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 1.0.0-1
- Initial package
