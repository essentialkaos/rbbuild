### RBBuild

`rbbuild` is utility for compiling and installing different ruby versions.

#### Installation

###### From ESSENTIAL KAOS Public repo for RHEL6/CentOS6

```
yum install -y http://release.yum.kaos.io/i386/kaos-repo-6.8-0.el6.noarch.rpm
yum install rbbuild
```

#### Usage

```
Usage: rbbuild <definition-file> <options>...

Options:

  --prefix, -p path             Path where you want to install selected ruby version
  --dest-dir, -d path           Path where you want to install selected ruby version (used for 'make install')
  --threads, -t num             Number of threads for build process
  --no-patch, -np               Skip patch directives in definition file
  --cc-comp, -cc path/name      Path to C compiler
  --cxx-comp, -cxx path         Path to C++ compiler
  --ignore-checksums, -ic       Skip checksum check (insecure!)
  --list, -l                    List of all definition files
  --mirror, -m name             Mirror name for downloading source archives from it
  --mirror-list, -ml            Show list of all available mirrors
  --dl-cache, -dc path          Path to download cache
  --rbenv, -r                   Automatically install to rbenv (--prefix not required)
  --name, -rn name              Define name of ruby in rbenv (--rbenv required)
  --strict, -S                  Fail build if configure stage return non zero exit code
  --proxy, -P url               Use HTTP proxy on given host and port
  --debug, -D                   Don't remove build directory and other build data after installation
  --output, -O path             Output path (default /dev/stdout)
  --quiet, -q                   Quiet mode
  --verbose, -V                 Verbose mode
  --tmp, -T path                Path to temporary directory (used for unpacking files and build process)
  --yes, -y                     Answer "yes" to all questions
  --no-colors, -C               Don't use colors in output
  --help, -h                    Show this help message
  --version, -v                 Show information about version

Examples:

  rbbuild 2.1.1-p0 -t 4 -m somemirror
  rbbuild 2.1.1-p0 -t 8 -r -cc clang
  rbbuild 2.1.1-p0 -p /home/user/ruby-2.1.1
  rbbuild 2.1.1-p0 -r mysuper-2.2.1
  rbbuild 1.9.3
```

#### License

[EKOL](https://essentialkaos.com/ekol)
