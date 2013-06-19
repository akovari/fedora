These are some dummy scripts to find which gems that [GitLab][gitlab] is using, are missing from Fedora repositories.

On a Fedora machine, clone the repository, cd into it and run:

```  
sudo yum install python2 python-bugzilla
chmod +x run.sh
./run.sh
```

More info in my [blogpost][].

[blogpost]: http://axilleas.github.io/en/blog/2013/bringing-gitlab-in-fedora
[gitlab]: https://github.com/gitlabhq/gitlabhq
