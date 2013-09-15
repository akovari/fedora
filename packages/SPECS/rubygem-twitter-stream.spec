# Generated from twitter-stream-0.1.16.gem by gem2rpm -*- rpm-spec -*-
%global gem_name twitter-stream

Name: rubygem-%{gem_name}
Version: 0.1.16
Release: 1%{?dist}
Summary: Twitter realtime API client
Group: Development/Languages
License: MIT
URL: http://github.com/voloko/twitter-stream
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) >= 1.3.6
Requires: rubygem(eventmachine) >= 0.12.8
# Update simple_oauth dependency
# https://github.com/voloko/twitter-stream/pull/37
Requires: rubygem(simple_oauth) => 0.2
Requires: rubygem(simple_oauth) < 0.3
Requires: rubygem(http_parser.rb) => 0.5.1
Requires: rubygem(http_parser.rb) < 0.6
BuildRequires: ruby(release)
BuildRequires: rubygems-devel >= 1.3.6
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(eventmachine)
BuildRequires: rubygem(simple_oauth)
BuildRequires: rubygem(http_parser.rb)
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Simple Ruby client library for twitter streaming API. Uses EventMachine for
connection handling. Adheres to twitter's reconnection guidline. JSON format
only.

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

%check
pushd .%{gem_instdir}
rspec spec/
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/LICENSE
%{gem_spec}
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.markdown
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/spec/
%{gem_instdir}/examples/
%{gem_instdir}/fixtures/
%exclude %{gem_instdir}/VERSION

%changelog
* Wed Aug 14 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 0.1.16-1
- Initial package
