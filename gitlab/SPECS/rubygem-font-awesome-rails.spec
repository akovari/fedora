# Generated from font-awesome-rails-3.2.1.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name font-awesome-rails

Name: rubygem-%{gem_name}
Version: 3.2.1.2
Release: 1%{?dist}
Summary: An asset gemification of the font-awesome icon font library.
Group: Development/Languages
License: MIT and SIL Open Font License
URL: https://github.com/bokmann/font-awesome-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(railties) >= 3.2
Requires: rubygem(railties) < 5.0
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildRequires: rubygem(minitest) 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
I like font-awesome. I like the asset pipeline. I like semantic versioning. If
you do too, you're welcome.


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
#testrb2 -Ilib test/
popd


%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_spec}
%doc %{gem_instdir}/LICENSE
%{gem_instdir}/app/
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test/


%changelog
* Fri Aug 09 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 3.2.1.2-1
- Initial package
