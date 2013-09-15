# Generated from raphael-rails-2.1.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name raphael-rails

Name: rubygem-%{gem_name}
Version: 2.1.1
Release: 1%{?dist}
Summary: Raphael JS as a Rubygem
Group: Development/Languages
License: MIT
URL: https://github.com/mockdeep/raphael-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Raphael JS as a Rubygem for use in the Rails asset pipeline


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

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/license.txt
%{gem_spec}
%{gem_instdir}/vendor/
%exclude %{gem_cache}
%exclude %{gem_instdir}/vendor/assets/javascripts/README.markdown
%exclude %{gem_instdir}/vendor/assets/javascripts/history.md
%exclude %{gem_instdir}/vendor/assets/javascripts/reference.html
%exclude %{gem_instdir}/vendor/assets/javascripts/license.txt


%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/vendor/assets/javascripts/history.md
%doc %{gem_instdir}/vendor/assets/javascripts/reference.html
%doc %{gem_instdir}/README.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile

%changelog
* Mon Aug 19 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 2.1.1-1
- Initial package
