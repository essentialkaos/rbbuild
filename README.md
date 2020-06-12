<p align="center"><a href="#readme"><img src="https://gh.kaos.st/rbbuild.svg"/></a></p>

<p align="center">
  <a href="https://travis-ci.com/essentialkaos/rbbuild"><img src="https://travis-ci.com/essentialkaos/rbbuild.svg"></a>
  <a href="https://essentialkaos.com/ekol"><img src="https://gh.kaos.st/ekol.svg"></a>
</p>

<p align="center"><a href="#usage-demo">Usage demo</a> • <a href="#installation">Installation</a> • <a href="#usage">Usage</a> • <a href="#build-status">Build Status</a> • <a href="#license">License</a></p>

<br/>

`rbbuild` is utility for compiling and installing different Ruby versions.

### Usage demo

[![demo](https://gh.kaos.st/rbbuild-180.gif)](#usage-demo)

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
Usage: rbbuild {definition-file} {options}...

Options:

  --prefix, -p path           Path where you want to install selected ruby version
  --dest-dir, -d path         Path where you want to install selected ruby version (used for 'make install')
  --threads, -t num           Number of threads for build process
  --no-patch, -np             Skip patch directives in definition file
  --cc-comp, -cc path/name    Path to C compiler
  --cxx-comp, -cxx path       Path to C++ compiler
  --ignore-checksums, -ic     Skip checksum check (insecure!)
  --list, -l                  List of all definition files
  --mirror, -m name           Mirror name for downloading source archives from it
  --mirror-list, -ml          Show list of all available mirrors
  --dl-cache, -dc path        Path to download cache
  --rbenv, -r                 Automatically install to rbenv (--prefix not required)
  --name, -rn name            Define name of ruby in rbenv (--rbenv required)
  --strict, -S                Fail build if configure stage return non zero exit code
  --proxy, -P url             Use HTTP proxy on given host and port
  --debug, -D                 Don't remove build directory and other build data after installation
  --output, -O path           Output path (default /dev/stdout)
  --quiet, -q                 Quiet mode
  --verbose, -V               Verbose mode
  --tmp, -T path              Path to temporary directory (used for unpacking files and build process)
  --yes, -y                   Answer "yes" to all questions
  --no-colors, -nc            Don't use colors in output
  --help, -h                  Show this help message
  --version, -v               Show information about version

Examples:

  rbbuild 2.1.1-p0 -t 4 -m somemirror
  rbbuild 2.1.1-p0 -t 8 -r -cc clang
  rbbuild 2.1.1-p0 -p /home/user/ruby-2.1.1
  rbbuild 2.1.1-p0 -r mysuper-2.2.1
  rbbuild 1.9.3

```

### Build Status

| Branch | Status |
|--------|--------|
| `master` | [![Build Status](https://travis-ci.com/essentialkaos/rbbuild.svg?branch=master)](https://travis-ci.com/essentialkaos/rbbuild) |
| `develop` | [![Build Status](https://travis-ci.com/essentialkaos/rbbuild.svg?branch=develop)](https://travis-ci.com/essentialkaos/rbbuild) |

### License

[EKOL](https://essentialkaos.com/ekol)

<p align="center"><a href="https://essentialkaos.com"><img src="https://gh.kaos.st/ekgh.svg"/></a></p>
