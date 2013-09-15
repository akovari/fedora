# Generated from http_parser.rb-0.5.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name http_parser.rb

Name: rubygem-%{gem_name}
Version: 0.5.3
Release: 1%{?dist}
Summary: Simple callback-based HTTP request/response parser
Group: Development/Languages
License: MIT
URL: http://github.com/tmm1/http_parser.rb
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby-devel 
BuildRequires: rubygem(rspec) 
Provides: rubygem(%{gem_name}) = %{version}

%description
Ruby bindings to http://github.com/ry/http-parser and
http://github.com/a2800276/http-parser.java


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

mkdir -p %{buildroot}%{gem_extdir_mri}/lib
mv %{buildroot}%{gem_libdir}/ruby_http_parser.so %{buildroot}%{gem_extdir_mri}/lib/ruby_http_parser.so

# Remove ext
rm -rf %{buildroot}%{gem_instdir}/ext/

%check
pushd .%{gem_instdir}
LANG=en_US.utf8
rspec spec/
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/LICENSE-MIT
%{gem_extdir_mri}
%{gem_spec}
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Gemfile.lock
%{gem_instdir}/Rakefile
%{gem_instdir}/spec/
%{gem_instdir}/bench/
%{gem_instdir}/tasks/
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Sat Aug 10 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 0.5.3-1
- Initial package
