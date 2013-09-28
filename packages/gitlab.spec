%global apprundir %{_var}/run/%{name}
%global homedir   %{_datadir}/%{name}
%global repodir   %{_sharedstatedir}/%{name}
%global confdir   %{_sysconfdir}/%{name}
%global logdir    %{_localstatedir}/log/%{name}

Summary: Self hosted Git management software
Name: gitlab
Version: 6.1.0
Release: 2%{?dist}
Group: Applications/Internet
License: MIT
URL: http://www.gitlab.org
Source0: https://github.com/gitlabhq/gitlabhq/archive/v%{version}.tar.gz
Source1: gitlab-sidekiq.service
Source2: gitlab-unicorn.service
Patch0: gitlab-6.1.0-change-versions-in-gemfile.patch
Patch1: gitlab-6.1.0-change-versions-in-gemfile.lock.patch
BuildArch: noarch
Provides: gitlab = %{version}-%{release}

Requires: ruby(release)
Requires: systemd-units

# regular packages
Requires: git
Requires: openssh-server
Requires: redis
Requires: python
Requires: python-docutils
Requires: gitlab-shell

# gems
Requires: rubygem(rails)
Requires: rubygem(mysql2)
Requires: rubygem(pg)
Requires: rubygem(devise)
Requires: rubygem(omniauth)
Requires: rubygem(omniauth-google-oauth2)
Requires: rubygem(omniauth-twitter)
Requires: rubygem(omniauth-github)
Requires: rubygem(gitlab_git)
Requires: rubygem(gitlab-grack)
Requires: rubygem(gitlab_omniauth-ldap)
Requires: rubygem(gitlab-pygments.rb)
Requires: rubygem(gitlab-gollum-lib)
Requires: rubygem(github-linguist)
Requires: rubygem(grape)
Requires: rubygem(grape-entity)
Requires: rubygem(stamp)
Requires: rubygem(enumerize)
Requires: rubygem(kaminari)
Requires: rubygem(haml-rails)
Requires: rubygem(carrierwave)
Requires: rubygem(six)
Requires: rubygem(seed-fu)
Requires: rubygem(redcarpet)
Requires: rubygem(github-markup)
Requires: rubygem(asciidoctor)
Requires: rubygem(unicorn)
Requires: rubygem(state_machine)
Requires: rubygem(acts-as-taggable-on)
Requires: rubygem(slim)
Requires: rubygem(sinatra)
Requires: rubygem(sidekiq)
Requires: rubygem(httparty)
Requires: rubygem(colored)
Requires: rubygem(settingslogic)
Requires: rubygem(foreman)
Requires: rubygem(redis-rails)
#Requires: rubygem(tinder)
Requires: rubygem(hipchat)
Requires: rubygem(d3_rails)
Requires: rubygem(underscore-rails)
Requires: rubygem(sanitize)
Requires: rubygem(sass-rails)
Requires: rubygem(coffee-rails)
Requires: rubygem(uglifier)
Requires: rubygem(therubyracer)
Requires: rubygem(turbolinks)
Requires: rubygem(jquery-turbolinks)
Requires: rubygem(chosen-rails)
Requires: rubygem(select2-rails)
Requires: rubygem(jquery-atwho-rails)
Requires: rubygem(jquery-rails)
Requires: rubygem(jquery-ui-rails)
Requires: rubygem(modernizr)
Requires: rubygem(raphael-rails)
Requires: rubygem(bootstrap-sass)
Requires: rubygem(font-awesome-rails)
Requires: rubygem(gemoji)
Requires: rubygem(gon)
BuildRequires: ruby(release)
BuildRequires: ruby-devel
BuildRequires: ruby
BuildRequires: systemd-units

# Filter /usr/bin/env/ from RPM's autorequires.
%global __requires_exclude ^/usr/bin/env$

%description
Self hosted Git management software

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -q -n gitlabhq-%{version}

%patch0
%patch1

%build

%install
# Prepare dir structure
install -d -m0755 %{buildroot}%{homedir}
install -d -m0755 %{buildroot}%{homedir}/%{name}
install -d -m0755 %{buildroot}%{homedir}/%{name}/tmp/
install -d -m0755 %{buildroot}%{homedir}/%{name}/tmp/pids
install -d -m0755 %{buildroot}%{homedir}/%{name}/tmp/sockets
install -d -m0755 %{buildroot}%{homedir}/%{name}/log/
install -d -m0755 %{buildroot}%{homedir}/%{name}/public/uploads/
install -d -m0755 %{buildroot}%{confdir}
install -d -m0755 %{buildroot}%{logdir}
install -d -m0755 %{buildroot}%{apprundir}

# Fix permissions
chmod -R u+rwX %{buildroot}%{homedir}/%{name}/{tmp,log}
chmod -R u+rwX %{buildroot}%{homedir}/%{name}/public/uploads

# Configure Git global settings for gitlab user, useful when editing via web ui
cat > %{buildroot}%{homedir}/.gitconfig << EOF
[user]
  name "GitLab"
  email "gitlab@localhost"
[core]
  autocrlf input
EOF

# Copy all files to homedir
cp -a * %{buildroot}%{homedir}/%{name}

# Copy mysql config to /etc/gitlab/
install -Dm644 %{buildroot}%{homedir}/%{name}/config/database.yml.mysql %{buildroot}%{confdir}/database.yml

# For postrges
#install -Dm644 %{buildroot}%{homedir}/%{name}/config/database.yml.postgresql %{confdir}/database.yml

# Change pid/log paths in unicorn.rb and copy config to /etc/gitlab/
sed -e "s|working_directory \"/home/git/gitlab\"|working_directory \"/usr/share/gitlab/gitlab\"|" \
    -e "s|\"/home/git/gitlab/tmp/sockets/gitlab.socket\"|\"/var/run/gitlab/gitlab.socket\"|" \
    -e "s|\"/home/git/gitlab/tmp/pids/unicorn.pid\"|\"/var/run/gitlab/unicorn.pid\"|" \
    -e "s|/home/git/gitlab/log|/var/log/gitlab|g" \
    config/unicorn.rb.example > %{buildroot}%{confdir}/unicorn.rb

# Change paths in gitlab.yml and copy config to /etc/gitlab/
sed -e "s|# user: git|user: gitlab|" \
    -e "s|/home/git/repositories|%{repodir}/repositories|" \
    -e "s|/home/git/gitlab-satellites|%{repodir}/satellites|" \
    -e "s|/home/git|%{repodir}|" \
    config/gitlab.yml.example > %{buildroot}%{confdir}/%{name}.yml

# Make symlinks to gitlab app root dir
for conf in gitlab.yml database.yml unicorn.rb; do
  ln -svf %{confdir}/$conf %{buildroot}%{homedir}/%{name}/config/
done

# systemd files
mkdir -p %{buildroot}%{_unitdir}
install -m644 %{SOURCE1} %{buildroot}%{_unitdir}
install -m644 %{SOURCE2} %{buildroot}%{_unitdir}

# Remove hidden .gitkeep files
find %{buildroot}%{homedir}/%{name} -name '.gitkeep' | xargs rm

# Remove shebang from Rakefile
sed -i '1 d' %{buildroot}%{homedir}/%{name}/Rakefile


%post
systemctl --system daemon-reload

%files
%dir %{homedir}/
%dir %{homedir}/%{name}
%dir %{confdir}
%dir %{logdir}
%config(noreplace) %{confdir}/gitlab.yml
%config(noreplace) %{confdir}/database.yml
%config(noreplace) %{confdir}/unicorn.rb
%doc %{homedir}/%{name}/LICENSE
%doc %{homedir}/%{name}/VERSION
%{homedir}/.gitconfig
%{homedir}/%{name}/vendor/
%{homedir}/%{name}/lib/
%{homedir}/%{name}/app/
%{homedir}/%{name}/db/
%{homedir}/%{name}/log/
%{homedir}/%{name}/public/
%{homedir}/%{name}/tmp/
%{homedir}/%{name}/config
%{homedir}/%{name}/script/
%{homedir}/%{name}/config.ru
%{_unitdir}/%{name}-unicorn.service
%{_unitdir}/%{name}-sidekiq.service
%{homedir}/%{name}/Gemfile
%{homedir}/%{name}/Gemfile.lock
%{homedir}/%{name}/Rakefile
%exclude %{homedir}/%{name}/.*
%exclude %{homedir}/%{name}/Guardfile
%exclude %{homedir}/%{name}/Procfile
# We don't need the init script. systemd baby!
%exclude %{homedir}/%{name}/lib/support/init.d/

%files doc
%{homedir}/%{name}/spec/
%{homedir}/%{name}/features/
%doc %{homedir}/%{name}/doc/
%doc %{homedir}/%{name}/CHANGELOG
%doc %{homedir}/%{name}/CONTRIBUTING.md
%doc %{homedir}/%{name}/MAINTENANCE.md
%doc %{homedir}/%{name}/PROCESS.md
%doc %{homedir}/%{name}/README.md

%changelog
* Wed Sep 25 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 6.1.0-2
- Drop versioned dependencies

* Tue Sep 24 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 6.1.0-1
- Update to 6.1.0

* Sat Sep 21 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 6.0.2-2
- Add new dir: /var/log/gitlab/
- Replace pid/log/socket paths in unicorn.rb
- Filter /usr/bin/env/ from RPM's autorequires
- gitlab-unicorn.service updated with the new paths
- gitlab-sidekiq.service updated with the new paths
- Add patches for Gemfile and Gemfile.lock

* Sat Sep 14 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 6.0.2-1
- Initial package
