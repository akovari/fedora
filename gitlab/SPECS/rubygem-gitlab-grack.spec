# Generated from gitlab-grack-1.0.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name gitlab-grack

Name: rubygem-%{gem_name}
Version: 1.0.1
Release: 1%{?dist}
Summary: Ruby/Rack Git Smart-HTTP Server Handler
Group: Development/Languages
License: MIT
URL: https://github.com/gitlabhq/grack
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems)
Requires: rubygem(rack) => 1.4.1
Requires: rubygem(rack) < 1.5
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
#BuildRequires: rubygem(rack)
#BuildRequires: rubygem(rack-test)
#BuildRequires: rubygem(test-unit)
#BuildRequires: rubygem(minitest)
#BuildRequires: rubygem(mocha)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Ruby/Rack Git Smart-HTTP Server Handler


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
#testrb2 -Ilib tests/main_test.rb
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_spec}
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/install.txt
%{gem_instdir}/Gemfile
%{gem_instdir}/Gemfile.lock
%{gem_instdir}/Rakefile
%{gem_instdir}/grack.gemspec
%{gem_instdir}/examples/
%{gem_instdir}/tests/

%changelog
* Wed Aug 21 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 1.0.1-1
- Initial package
