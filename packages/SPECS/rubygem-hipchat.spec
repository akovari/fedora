# Generated from hipchat-0.11.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name hipchat

Name: rubygem-%{gem_name}
Version: 0.11.0
Release: 1%{?dist}
Summary: Ruby library to interact with HipChat
Group: Development/Languages
License: MIT
URL: https://github.com/hipchat/hipchat-rb
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(httparty) 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(httparty)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Ruby library to interact with HipChat


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
%doc %{gem_instdir}/LICENSE
%{gem_spec}
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}


%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.textile
%{gem_instdir}/Gemfile
%{gem_instdir}/Gemfile.lock
%{gem_instdir}/Rakefile
%{gem_instdir}/spec/
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Sat Aug 10 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 0.11.0-1
- Initial package
