# Generated from gitlab_git-2.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name gitlab_git

Name: rubygem-%{gem_name}
Version: 2.1.1
Release: 1%{?dist}
Summary: Gitlab::Git library
Group: Development/Languages
License: MIT
URL: http://rubygems.org/gems/gitlab_git
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems)
Requires: rubygem(github-linguist) => 2.3.4
Requires: rubygem(github-linguist) < 2.10
Requires: rubygem(gitlab-grit) => 2.6.0
Requires: rubygem(gitlab-grit) < 2.7
Requires: rubygem(activesupport) => 3.2.13
Requires: rubygem(activesupport) < 3.3
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
#BuildRequires: rubygem(pry)
#BuildRequires: rubygem(simplecov)
#BuildRequires: rubygem(rspec)
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
GitLab wrapper around git objects


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

%changelog
* Fri Sep 06 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 2.1.1-1
- Update to 2.1.1

* Wed Aug 21 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 2.1.0-1
- Initial package
