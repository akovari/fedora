# Generated from bundler_ext-0.3.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name bundler_ext

Name: rubygem-%{gem_name}
Version: 0.3.1
Release: 1%{?dist}
Summary: Load system gems via Bundler DSL
Group: Development/Languages
License: MIT
URL: https://github.com/bundlerext/bundler_ext
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems)
Requires: rubygem(bundler)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(bundler)
BuildRequires: rubygem(rspec)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Simple library leveraging the Bundler Gemfile DSL to load gems already on the
system and managed by the systems package manager (like yum/apt)


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
rspec spec/
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/MIT-LICENSE
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/spec/

%changelog
* Wed Aug 21 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 0.3.1-1
- Initial package
