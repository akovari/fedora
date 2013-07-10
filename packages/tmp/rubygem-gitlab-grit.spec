# Generated from gitlab-grit-2.6.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name gitlab-grit

Name: rubygem-%{gem_name}
Version: 2.6.0
Release: 1%{?dist}
Summary: Ruby Git bindings
Group: Development/Languages
License: MIT
URL: http://github.com/gitlabhq/grit
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(charlock_holmes) => 0.6.9
Requires: rubygem(charlock_holmes) < 0.7
Requires: rubygem(posix-spawn) => 0.3.6
Requires: rubygem(posix-spawn) < 0.4
Requires: rubygem(mime-types) => 1.15
Requires: rubygem(mime-types) < 2
Requires: rubygem(diff-lcs) => 1.1
Requires: rubygem(diff-lcs) < 2
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Grit is a Ruby library for extracting information from a git repository in an
object oriented manner. GitLab fork


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
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/LICENSE

%changelog
* Mon Jul 08 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 2.6.0-1
- Initial package
