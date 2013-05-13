# Generated from gemoji-1.4.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name gemoji
%global rubyabi 1.9.1

Name: rubygem-%{gem_name}
Version: 1.4.0
Release: 1%{?dist}
Summary: Emoji Assets
Group: Development/Languages
License: 
URL: https://github.com/github/gemoji
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Emoji assets


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
mkdir -p .%{gem_dir}

# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec


# gem install installs into a directory.  We set that to be a local
# directory so that we can move it into the buildroot in %%install
gem install --local --install-dir ./%{gem_dir} \
            --force --rdoc %{gem_name}-%{version}.gem

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
* Sun May 05 2013 axilleas@archlinux.gr - 1.4.0-1
- Initial package
