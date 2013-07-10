# Generated from celluloid-0.14.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name celluloid

Name: rubygem-%{gem_name}
Version: 0.14.1
Release: 1%{?dist}
Summary: Actor-based concurrent object framework for Ruby
Group: Development/Languages
License: MIT
URL: https://github.com/celluloid/celluloid
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) >= 1.3.6
Requires: rubygem(timers) >= 1.0.0
BuildRequires: ruby(release)
BuildRequires: rubygems-devel >= 1.3.6
BuildRequires: ruby >= 1.9.2
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Celluloid enables people to build concurrent programs out of concurrent
objects just as easily as they build sequential programs out of sequential
objects


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




%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
* Mon Jul 08 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 0.14.1-1
- Initial package
