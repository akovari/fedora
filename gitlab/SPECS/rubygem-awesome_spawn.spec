# Generated from awesome_spawn-1.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name awesome_spawn

Name: rubygem-%{gem_name}
Version: 1.0.0
Release: 2%{?dist}
Summary: A module that provides some useful features over Ruby's Kernel.spawn
Group: Development/Languages
License: MIT
URL: https://github.com/ManageIQ/awesome_spawn
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: rubygems
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
AwesomeSpawn is a module that provides some useful features over Ruby's
Kernel.spawn.

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

# Remove developer-only files.
for f in .rspec .travis.yml .yardopts .gitignore Gemfile Rakefile; do
  rm $f
  sed -i "s|\"$f\",||g" %{gem_name}.gemspec
done

%build

# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

%gem_install

# Remove unnecessary gemspec file
rm .%{gem_instdir}/%{gem_name}.gemspec

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
sed -i '/[Cc]overalls/d' spec/spec_helper.rb
rspec spec/
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/LICENSE.txt
%doc %{gem_instdir}/README.md
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/spec/

%changelog
* Tue Jan 21 2014 Achilleas Pipinellis <axilleaspi@ymail.com> - 1.0.0-2
- Remove unecessary comments
- Fix Requires/BuildRequires typos

* Sun Jan 19 2014 Achilleas Pipinellis <axilleaspi@ymail.com> - 1.0.0-1
- Initial package
