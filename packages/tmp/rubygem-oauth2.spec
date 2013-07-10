# Generated from oauth2-0.9.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name oauth2

Name: rubygem-%{gem_name}
Version: 0.9.2
Release: 1%{?dist}
Summary: A Ruby wrapper for the OAuth 2.0 protocol
Group: Development/Languages
License: MIT
URL: http://github.com/intridea/oauth2
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) >= 1.3.5
Requires: rubygem(faraday) => 0.8
Requires: rubygem(faraday) < 1
Requires: rubygem(httpauth) => 0.2
Requires: rubygem(httpauth) < 1
Requires: rubygem(multi_json) => 1.0
Requires: rubygem(multi_json) < 2
Requires: rubygem(multi_xml) => 0.5
Requires: rubygem(multi_xml) < 1
Requires: rubygem(rack) => 1.2
Requires: rubygem(rack) < 2
Requires: rubygem(jwt) => 0.1.4
Requires: rubygem(jwt) < 0.2
BuildRequires: ruby(release)
BuildRequires: rubygems-devel >= 1.3.5
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
A Ruby wrapper for the OAuth 2.0 protocol built with a similar style to the
original OAuth spec.


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
* Mon Jul 08 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 0.9.2-1
- Initial package
