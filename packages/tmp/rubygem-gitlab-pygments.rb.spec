# Generated from gitlab-pygments.rb-0.3.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name gitlab-pygments.rb

Name: rubygem-%{gem_name}
Version: 0.3.2
Release: 1%{?dist}
Summary: pygments wrapper for ruby
Group: Development/Languages
License: 
URL: http://github.com/gitlabhq/pygments.rb
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(yajl-ruby) => 1.1.0
Requires: rubygem(yajl-ruby) < 1.2
Requires: rubygem(posix-spawn) => 0.3.6
Requires: rubygem(posix-spawn) < 0.4
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
pygments.rb exposes the pygments syntax highlighter to Ruby


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

%changelog
* Mon Jul 08 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 0.3.2-1
- Initial package
