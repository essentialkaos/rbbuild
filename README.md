<p align="center"><a href="#readme"><img src="https://gh.kaos.st/rbbuild.svg"/></a></p>

<p align="center">
  <a href="https://kaos.sh/w/rbbuild/ci"><img src="https://kaos.sh/w/rbbuild/ci.svg" alt="GitHub Actions CI Status" /></a>
  <a href="#license"><img src="https://gh.kaos.st/apache2.svg"></a>
</p>

<p align="center"><a href="#usage-demo">Usage demo</a> • <a href="#installation">Installation</a> • <a href="#usage">Usage</a> • <a href="#ci-status">CI Status</a> • <a href="#license">License</a></p>

<br/>

`rbbuild` is utility for compiling and installing different Ruby versions.

### Usage demo

[![demo](https://gh.kaos.st/rbbuild-200.gif)](#usage-demo)

### Installation

#### From [ESSENTIAL KAOS Public Repository](https://pkgs.kaos.st)

```bash
sudo yum install -y https://pkgs.kaos.st/kaos-repo-latest.el$(grep 'CPE_NAME' /etc/os-release | tr -d '"' | cut -d':' -f5).noarch.rpm
sudo yum install rbbuild
```

#### Using Makefile and Git

```bash
git clone https://kaos.sh/rbbuild.git
cd rbbuild
sudo make install
```

### Usage

```
Usage: rbbuild {options} def-file target-dir

Options

  --threads, -t num           Number of threads for build process
  --no-patch, -np             Skip patch directives in definition file
  --cc-comp, -cc path/name    Path to C compiler
  --cxx-comp, -cxx path       Path to C++ compiler
  --ignore-checksums, -ic     Skip checksum check
  --ignore-loadavg, -il       Ignore check for high LA
  --mirror, -m name           Mirror name for downloading source archives from it
  --mirror-list, -L           Show list of all available mirrors
  --dl-cache, -dc path        Path to download cache
  --rbenv, -r                 Automatically install to RBEnv
  --name, -rn name            Define name of ruby in RBEnv (--rbenv is required)
  --proxy, -P url             Use HTTP proxy on given host and port
  --debug, -D                 Don't remove build directory and other build data after installation
  --output, -O path           Output path (default /dev/stdout)
  --quiet, -q                 Quiet mode
  --verbose, -V               Verbose mode
  --tmp, -T path              Path to temporary directory (used for unpacking files and build process)
  --yes, -y                   Answer "yes" to all questions
  --continue, -C              Don't clean prefix directory before build
  --no-colors, -nc            Don't use colors in output
  --no-spinner, -ns           Don't show spinner
  --help, -h                  Show this help message
  --version, -v               Show information about version

Examples

  rbbuild 2.7.5 /home/user/ruby-2.7.5 -t 4 -m essentialkaos
  Build 2.7.5 with sources from EK mirror using 4 threads

  rbbuild 3.0.5 /home/user/ruby-3.0.5
  Build 3.0.5 and install it to given directory

  rbbuild 3.1.1 -r
  Build 3.1.1 and install it to RBEnv

  rbbuild 3.1.1 | more
  Show def file for 3.1.1
```

### CI Status

| Branch | Status |
|--------|--------|
| `master` | [![CI](https://kaos.sh/w/rbbuild/ci.svg?branch=master)](https://kaos.sh/w/rbbuild/ci?query=branch:master) |
| `develop` | [![CI](https://kaos.sh/w/rbbuild/ci.svg?branch=master)](https://kaos.sh/w/rbbuild/ci?query=branch:develop) |

### License

[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)

<p align="center"><a href="https://essentialkaos.com"><img src="https://gh.kaos.st/ekgh.svg"/></a></p>
