# Generated from timers-1.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name timers

Name: rubygem-%{gem_name}
Version: 2.0.0
Release: %{?dist}
Summary: Pure Ruby one-shot and periodic timers
Group: Development/Languages
License: MIT
URL: https://github.com/celluloid/timers
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: rubygems
Requires: rubygem(hitimes)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Schedule procs to run after a certain time using any API that accepts a timeout

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

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

chmod 755 %{buildroot}%{gem_instdir}/Rakefile

%check
pushd .%{gem_instdir}

# Bundler is used only for development. No need to install it.
sed -i '/bundler/d' spec/spec_helper.rb

rspec spec/
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_spec}
%doc %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGES.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/Gemfile
%{gem_instdir}/spec/
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Mon Jan 20 2014 Achilleas Pipinellis <axilleaspi@ymail.com> - 2.0.0-1
- Bump version
- Clean up spec

* Mon Jun 03 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 1.1.0-2
- Fix Summary/Description tags

* Thu May 30 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 1.1.0-1
- Initial package
