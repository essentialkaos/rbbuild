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

#### `rbbuild`

<img src=".github/images/rbbuild.svg" />

#### `rbdef`

<img src=".github/images/rbdef.svg" />

#### `mass-builder`

<img src=".github/images/mass-builder.svg" />

### CI Status

| Branch | Status |
|--------|--------|
| `master` | [![CI](https://kaos.sh/w/rbbuild/ci.svg?branch=master)](https://kaos.sh/w/rbbuild/ci?query=branch:master) |
| `develop` | [![CI](https://kaos.sh/w/rbbuild/ci.svg?branch=master)](https://kaos.sh/w/rbbuild/ci?query=branch:develop) |

### License

[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)

<p align="center"><a href="https://essentialkaos.com"><img src="https://gh.kaos.st/ekgh.svg"/></a></p>
