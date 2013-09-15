# Generated from virtus-0.5.5.gem by gem2rpm -*- rpm-spec -*-
%global gem_name virtus

Name: rubygem-%{gem_name}
Version: 0.5.5
Release: 1%{?dist}
Summary: Attributes on Steroids for Plain Old Ruby Objects
Group: Development/Languages
License: MIT
URL: https://github.com/solnic/virtus
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(backports) => 3.3
Requires: rubygem(backports) < 4
Requires: rubygem(descendants_tracker) => 0.0.1
Requires: rubygem(descendants_tracker) < 0.1
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildRequires: rubygem(backports)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(simplecov)
BuildRequires: rubygem(descendants_tracker)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Attributes on Steroids for Plain Old Ruby Objects


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
# Remove coveralls
sed -i '/[Cc]overalls/d' spec/spec_helper.rb
rspec spec/
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/LICENSE
%{gem_instdir}/config/
%{gem_spec}
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/TODO
%doc %{gem_instdir}/Changelog.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Gemfile.devtools
%{gem_instdir}/Rakefile
%{gem_instdir}/Guardfile
%{gem_instdir}/spec/
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Sat Aug 10 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 0.5.5-1
- Initial package
