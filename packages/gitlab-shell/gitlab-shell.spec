%global homedir %{_datadir}/gitlab
%global repodir %{_sharedstatedir}/gitlab
%global confdir %{_sysconfdir}/gitlab

Summary:       ssh access and repository management for GitLab
Name:          gitlab-shell
Version:       1.7.1
Release:       1%{?dist}
Group:         Applications/Internet
License:       MIT
URL:           https://github.com/gitlabhq/gitlab-shell
Source0:       https://github.com/gitlabhq/gitlab-shell/archive/v%{version}.tar.gz
Requires: ruby(release)
Requires: git
Requires: redis
Requires(post): shadow-utils
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(vcr)
BuildArch: noarch
Provides: %{name} = %{version}-%{release}

%description
ssh access and repository management for use with GitLab

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -q

%build

%install

# Prepare directory structure
install -dm755 %{buildroot}%{homedir}
install -dm755 %{buildroot}%{homedir}/%{name}
install -dm770 %{buildroot}%{repodir}
install -dm700 %{buildroot}%{repodir}/.ssh/
install -dm770 %{buildroot}%{repodir}/repositories
install -dm770 %{buildroot}%{repodir}/satellites
install -dm755 %{buildroot}%{confdir}
touch %{buildroot}%{repodir}/.ssh/authorized_keys
chmod 600 %{buildroot}%{repodir}/.ssh/authorized_keys
chmod g+s %{buildroot}%{repodir}/repositories

# Change paths in config file
sed -e "s|user: git|user: gitlab|" \
    -e "s|/home/git/repositories|%{repodir}/repositories|" \
    -e "s|/home/git|%{repodir}|" \
    config.yml.example > %{buildroot}%{confdir}/%{name}.yml

ln -s %{confdir}/%{name}.yml %{buildroot}%{homedir}/%{name}/config.yml

cp -a CHANGELOG LICENSE README.md VERSION bin hooks lib spec support %{buildroot}%{homedir}/%{name}


%check
#pushd %{buildroot}%{homedir}/%{name}
# Copy needed config.yml
sed -e "s|user: git|user: gitlab|" \
    -e "s|/home/git/repositories|%{buildroot}%{repodir}/repositories|" \
   -e "s|/home/git|%{buildroot}%{repodir}|" \
    config.yml.example > config.yml
rspec spec/
#popd

%post
# Add the "gitlab" user and group
getent group gitlab >/dev/null 2>&1 || groupadd -r gitlab &>/dev/null
getent passwd gitlab >/dev/null 2>&1 || \
    useradd -r -g gitlab -d %{homedir} -s /sbin/nologin -c "GitLab" gitlab &>/dev/null
chown -R gitlab:gitlab %{homedir}
chown -R gitlab:gitlab %{repodir}
chmod -R go-rwx %{repodir}/.ssh/
chmod g+s %{repodir}/repositories/
exit 0


#%postun
#if getent passwd gitlab >/dev/null 2>&1; then
#  userdel gitlab >/dev/null 2>&1
#  rm -r %{homedir}
#fi
#if getent group gitlab >/dev/null 2>&1; then
#  groupdel gitlab >/dev/null 2>&1
#fi
#exit 0

%files
#%defattr(-,gitlab,gitlab,-)
%config(noreplace) %{confdir}/%{name}.yml
%config(noreplace) %{repodir}/.ssh/authorized_keys
# /var/lib/gitlab
%dir %{repodir}
%dir %{repodir}/repositories/
%dir %{repodir}/satellites/
%dir %{repodir}/.ssh/
%{repodir}/.ssh/authorized_keys
# /usr/share/gitlab
%dir %{homedir}
%dir %{homedir}/%{name}/bin/
%dir %{homedir}/%{name}/lib/
%dir %{homedir}/%{name}/hooks/
%dir %{homedir}/%{name}/support/
%doc %{homedir}/%{name}/LICENSE
%{homedir}/%{name}/config.yml

%files doc
%doc %{homedir}/%{name}/README.md
%doc %{homedir}/%{name}/CHANGELOG
%doc %{homedir}/%{name}/VERSION
%{homedir}/%{name}/spec/

%changelog
* Sat Sep 14 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 1.7.1-1
- Initial package
