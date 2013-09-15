# Generated from pyu-ruby-sasl-0.0.3.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name pyu-ruby-sasl

Name: rubygem-%{gem_name}
Version: 0.0.3.3
Release: 1%{?dist}
Summary: SASL client library
Group: Development/Languages
License: MIT
URL: http://github.com/pyu10055/ruby-sasl/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
#BuildRequires: rubygem(rspec) 
#BuildRequires: rubygem(spec) 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Simple Authentication and Security Layer (RFC 4422)


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
#rspec spec/
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/README.markdown
%{gem_instdir}/spec/  

%changelog
* Sun Aug 11 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 0.0.3.3-1
- Initial package
