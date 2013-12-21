# Generated from yajl-ruby-1.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name yajl-ruby

Name: rubygem-%{gem_name}
Version: 1.1.0
Release: 1%{?dist}
Summary: Ruby C bindings to the excellent Yajl JSON stream-based parser library
Group: Development/Languages
License: MIT 
URL: http://github.com/brianmario/yajl-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby-devel >= 1.8.6
BuildRequires: rubygem(rspec)
Provides: rubygem(%{gem_name}) = %{version}

%description
Ruby C bindings to the excellent Yajl JSON stream-based parser library.

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

mkdir -p %{buildroot}%{gem_extdir_mri}/lib/yajl/
mv %{buildroot}%{gem_libdir}/yajl/yajl.so %{buildroot}%{gem_extdir_mri}/lib/yajl/yajl.so

rm -rf %{buildroot}%{gem_instdir}/ext/

%check
pushd .%{gem_instdir}
rspec spec/
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_extdir_mri}
%{gem_spec}
%doc %{gem_instdir}/MIT-LICENSE
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/spec/
%{gem_instdir}/tasks/
%{gem_instdir}/benchmark/
%{gem_instdir}/examples/

%changelog
* Sun Aug 11 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 1.1.0-1
- Initial package
