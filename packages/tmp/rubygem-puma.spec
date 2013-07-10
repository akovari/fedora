# Generated from puma-2.0.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name puma

Name: rubygem-%{gem_name}
Version: 2.0.1
Release: 1%{?dist}
Summary: Puma is a simple, fast, and highly concurrent HTTP 1.1 server for Ruby web applications
Group: Development/Languages
License: BSD
URL: http://puma.io
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(rack) >= 1.1
Requires: rubygem(rack) < 2.0
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: openssl-devel 
BuildRequires: ruby-devel >= 1.8.7
Provides: rubygem(%{gem_name}) = %{version}

%description
Puma is a simple, fast, and highly concurrent HTTP 1.1 server for Ruby web
applications. It can be used with any application that supports Rack, and is
considered the replacement for Webrick and Mongrel. It was designed to be the
go-to server for [Rubinius](http://rubini.us), but also works well with JRuby
and MRI. Puma is intended for use in both development and production
environments.
Under the hood, Puma processes requests using a C-optimized Ragel extension
(inherited from Mongrel) that provides fast, accurate HTTP 1.1 protocol
parsing in a portable way. Puma then serves the request in a thread from an
internal thread pool (which you can control). This allows Puma to provide real
concurrency for your web application!
With Rubinius 2.0, Puma will utilize all cores on your CPU with real threads,
meaning you won't have to spawn multiple processes to increase throughput. You
can expect to see a similar benefit from JRuby.
On MRI, there is a Global Interpreter Lock (GIL) that ensures only one thread
can be run at a time. But if you're doing a lot of blocking IO (such as HTTP
calls to external APIs like Twitter), Puma still improves MRI's throughput by
allowing blocking IO to be run concurrently (EventMachine-based servers such
as Thin turn off this ability, requiring you to use special libraries). Your
mileage may vary. In order to get the best throughput, it is highly
recommended that you use a Ruby implementation with real threads like
[Rubinius](http://rubini.us) or [JRuby](http://jruby.org).


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

%check
pushd .


%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}/lib
# TODO: move the extensions
#mv %{buildroot}%{gem_instdir}/lib/shared_object.so %{buildroot}%{gem_extdir_mri}/lib/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%files
%dir %{gem_instdir}
%{gem_instdir}/bin
%{_bindir}/puma
%{_bindir}/pumactl
%{gem_libdir}
%{gem_extdir_mri}
%{gem_spec}
%{doc} %{gem_instdir}/LICENSE
%{doc} %{gem_instdir}/COPYING
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/ext
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/Manifest.txt
%doc %{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/Rakefile


%changelog
* Tue May 28 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 2.0.1-1
- Initial package
