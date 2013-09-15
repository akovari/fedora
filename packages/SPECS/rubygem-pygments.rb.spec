# Generated from pygments.rb-0.5.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name pygments.rb

Name: rubygem-%{gem_name}
Version: 0.5.2
Release: 2%{?dist}
Summary: pygments wrapper for ruby
Group: Development/Languages
License: MIT
URL: http://github.com/tmm1/pygments.rb
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
BuildRequires: rubygem(posix-spawn)
BuildRequires: rubygem(yajl-ruby)
BuildRequires: rubygem(test-unit)
BuildRequires: python
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

# The Python code in the vedor subdirectory references /usr/bin/lasso9.
# Filter this from RPM's autorequires.
%global __requires_exclude ^/usr/bin/lasso9$

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

%check
pushd .%{gem_instdir}
testrb2 -Ilib test/
popd


%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/LICENSE
%{gem_spec}
%{gem_instdir}/vendor/
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/test/
%{gem_instdir}/bench.rb
%{gem_instdir}/lexers
%{gem_instdir}/cache-lexers.rb

%changelog
* Sat Aug 31 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 0.5.2-2
- Exclude autorequires /usr/bin/lasso9

* Sun Aug 11 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 0.5.2-1
- Initial package
