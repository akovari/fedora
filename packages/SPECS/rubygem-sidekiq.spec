# Generated from sidekiq-2.13.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sidekiq

Name: rubygem-%{gem_name}
Version: 2.13.1
Release: 1%{?dist}
Summary: Simple, efficient background processing for Ruby
Group: Development/Languages
License: LGPL-3.0
URL: http://sidekiq.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(redis) >= 3.0
Requires: rubygem(redis-namespace) 
Requires: rubygem(connection_pool) >= 1.0.0
Requires: rubygem(celluloid) >= 0.14.1
Requires: rubygem(json) 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: rubygem(test-unit) 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Simple, efficient background processing for Ruby


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


mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
testrb2 -Ilib test/
popd

%files
%dir %{gem_instdir}
%{_bindir}/sidekiq
%{_bindir}/sidekiqctl
%{gem_instdir}/bin
%{gem_libdir}
%doc %{gem_instdir}/LICENSE
%{gem_spec}
%{gem_instdir}/web/
%exclude %{gem_instdir}/COMM-LICENSE
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Changes.md
%doc %{gem_instdir}/Contributing.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/test/
%{gem_instdir}/config.ru
%exclude %{gem_instdir}/Pro-Changes.md

%changelog
* Sun Aug 11 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 2.13.1-1
- Initial package
