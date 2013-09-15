# Generated from rubyntlm-0.3.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rubyntlm

Name: rubygem-%{gem_name}
Version: 0.1.1
Release: 1%{?dist}
Summary: Ruby/NTLM library
Group: Development/Languages
License: MIT
URL: https://github.com/winrb/rubyntlm
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby >= 1.8.7
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Ruby/NTLM provides message creator and parser for the NTLM authentication.


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
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README
%{gem_instdir}/Rakefile
%{gem_instdir}/test/
%{gem_instdir}/examples/

%changelog
* Sun Aug 11 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 0.3.4-1
- Initial package
