# Generated from tinder-1.9.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name tinder

Name: rubygem-%{gem_name}
Version: 1.9.2
Release: 1%{?dist}
Summary: Ruby wrapper for the Campfire API
Group: Development/Languages
License: MIT
URL: http://github.com/collectiveidea/tinder
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) >= 1.3.6
Requires: rubygem(eventmachine) => 1.0
Requires: rubygem(eventmachine) < 2
Requires: rubygem(faraday) => 0.8
Requires: rubygem(faraday) < 1
Requires: rubygem(faraday_middleware) => 0.9
Requires: rubygem(faraday_middleware) < 1
Requires: rubygem(hashie) => 1.0
Requires: rubygem(hashie) < 2
Requires: rubygem(json) => 1.7.5
Requires: rubygem(json) < 1.8
Requires: rubygem(mime-types) => 1.19
Requires: rubygem(mime-types) < 2
Requires: rubygem(multi_json) => 1.5
Requires: rubygem(multi_json) < 2
Requires: rubygem(twitter-stream) => 0.1
Requires: rubygem(twitter-stream) < 1
BuildRequires: ruby(release)
BuildRequires: rubygems-devel >= 1.3.6
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(faraday_middleware)
BuildRequires: rubygem(fakeweb)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
A Ruby API for interfacing with Campfire, the 37Signals chat application.


%package doc
Summary: Documentation for %{name}.
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
%{gem_spec}
%doc %{gem_instdir}/MIT-LICENSE
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.markdown
%doc %{gem_instdir}/CHANGELOG.txt
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/spec/
%{gem_instdir}/site/
%{gem_instdir}/init.rb

%changelog
* Wed Aug 14 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 1.9.2-1
- Initial package
