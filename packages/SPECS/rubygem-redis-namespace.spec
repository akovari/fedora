# Generated from redis-namespace-1.3.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name redis-namespace

Name: rubygem-%{gem_name}
Version: 1.3.1
Release: 1%{?dist}
Summary: Namespaces Redis commands
Group: Development/Languages
License: MIT
URL: http://github.com/resque/redis-namespace
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(redis) => 3.0.0
Requires: rubygem(redis) < 3.1
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(redis)
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Adds a Redis::Namespace class which can be used to namespace calls
to Redis. This is useful when using a single instance of Redis with
multiple, different applications.


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
sed -i '/[Bb]undler/d' spec/spec_helper.rb
#rspec spec/
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/LICENSE
%{gem_spec}
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/spec/

%changelog
* Sat Aug 10 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 1.3.1-1
- Initial package
