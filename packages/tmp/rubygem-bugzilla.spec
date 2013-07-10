# Generated from ruby-bugzilla-0.5.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ruby-bugzilla
%global fedora_name bugzilla

Name: rubygem-%{fedora_name}
Version: 0.5.2
Release: 1%{?dist}
Summary: Ruby binding for Bugzilla WebService APIs
Group: Development/Languages
License: LGPLv3+
URL: http://rubygems.org/ruby-bugzilla
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) >= 1.3.6
Requires: rubygem(gruff) 
Requires: rubygem(highline) 
Requires: rubygem(rmagick) 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel >= 1.3.6
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{fedora_name}) = %{version}

%description
This aims to provide similar features to access to Bugzilla through WebService
APIs in Ruby.


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


mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%files
%dir %{gem_instdir}
%{_bindir}/bzconsole
%{gem_instdir}/bin
%{gem_libdir}
%{gem_spec}
%doc %{gem_instdir}/COPYING
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*

%files doc
%doc %{gem_docdir}
%{gem_instdir}/README.rdoc
#%{gem_instdir}/Gemfile
#%{gem_instdir}/Rakefile
#%{gem_instdir}/spec/
#%{gem_instdir}/%{gem_name}.gemspec


%changelog
* Tue Jun 11 2013 axilleas@archlinux.gr - 0.5.2-1
- Initial package
