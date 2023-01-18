<p align="center"><a href="#readme"><img src="https://gh.kaos.st/rbbuild.svg"/></a></p>

<p align="center">
  <a href="https://kaos.sh/w/rbbuild/ci"><img src="https://kaos.sh/w/rbbuild/ci.svg" alt="GitHub Actions CI Status" /></a>
  <a href="#license"><img src="https://gh.kaos.st/apache2.svg"></a>
</p>

<p align="center"><a href="#usage-demo">Usage demo</a> • <a href="#installation">Installation</a> • <a href="#usage">Usage</a> • <a href="#build-status">Build Status</a> • <a href="#license">License</a></p>

<br/>

`rbbuild` is utility for compiling and installing different Ruby versions.

### Usage demo

[![demo](https://gh.kaos.st/rbbuild-200.gif)](#usage-demo)

### Installation

#### From [ESSENTIAL KAOS Public Repository](https://yum.kaos.st)

```bash
sudo yum install -y https://yum.kaos.st/get/$(uname -r).rpm
sudo yum install rbbuild
```

#### Using `install.sh`
We provide simple bash script `script.sh` for installing app from the sources.

```bash
# install p7zip, bash and gawk

git clone https://github.com/essentialkaos/rbbuild.git
cd rbbuild

sudo ./install.sh
```

If you have some issues with installing, try to use script in debug mode:

```bash
sudo ./install.sh --debug
```

### Usage

```
Usage: rbbuild {options} def-file target-dir

Options:

  --threads, -t num           Number of threads for build process
  --no-patch, -np             Skip patch directives in definition file
  --cc-comp, -cc path/name    Path to C compiler
  --cxx-comp, -cxx path       Path to C++ compiler
  --ignore-checksums, -ic     Skip checksum check
  --mirror, -m name           Mirror name for downloading source archives from it
  --mirror-list, -L           Show list of all available mirrors
  --dl-cache, -dc path        Path to download cache
  --rbenv, -r                 Automatically install to rbenv
  --name, -rn name            Define name of ruby in rbenv (--rbenv required)
  --proxy, -P url             Use HTTP proxy on given host and port
  --debug, -D                 Don't remove build directory and other build data after installation
  --output, -O path           Output path (default /dev/stdout)
  --quiet, -q                 Quiet mode
  --verbose, -V               Verbose mode
  --tmp, -T path              Path to temporary directory (used for unpacking files and build process)
  --yes, -y                   Answer "yes" to all questions
  --no-colors, -nc            Don't use colors in output
  --no-spinner, -ns           Don't show spinner
  --help, -h                  Show this help message
  --version, -v               Show information about version

Examples:

  rbbuild 2.7.5 /home/user/ruby-2.7.5 -t 4 -m essentialkaos -y
  rbbuild 3.0.5 /home/user/ruby-3.0.5
  rbbuild 3.1.1 -r
```

### Build Status

| Branch | Status |
|--------|--------|
| `master` | [![CI](https://kaos.sh/w/rbbuild/ci.svg?branch=master)](https://kaos.sh/w/rbbuild/ci?query=branch:master) |
| `develop` | [![CI](https://kaos.sh/w/rbbuild/ci.svg?branch=master)](https://kaos.sh/w/rbbuild/ci?query=branch:develop) |

### License

[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)

<p align="center"><a href="https://essentialkaos.com"><img src="https://gh.kaos.st/ekgh.svg"/></a></p>
