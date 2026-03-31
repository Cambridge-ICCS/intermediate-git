<img src="./assets/UCAM_ICCS_Logo.png"  width="600">

# Intermediate git

This repository contains documentation, resources, and code for the intermediate git session
designed and delivered by [Jack Atkinson](https://jackatkinson.net/) ([@jatkinson1000](https://github.com/jatkinson1000))
and Mikolaj Kowalski ([@Mikolaj-A-Kowalski](https://github.com/Mikolaj-A-Kowalski))
of [ICCS](https://github.com/Cambridge-ICCS).  
All materials, including slides and videos, are available such that individuals can cover the
course in their own time.

A website for this workshop can be found at
[cambridge-iccs.github.io/intermediate-git](https://cambridge-iccs.github.io/intermediate-git).


## Contents

- [Learning Objectives](#learning-objectives)
- [Teaching material](#teaching-material)
- [Preparation and prerequisites](#preparation-and-prerequisites)
- [Installation and setup](#installation-and-setup)
- [License information](#license)
- [Contribution Guidelines and Support](#contribution-guidelines-and-support)


## Learning Objectives

The key objective of this workshop is to provide you with knowledge of some of the
higher-level functionalities within git beyond basic usage.

We will achieve this through a presentation and accompanying hands-on exercises.
You will work on the code enclosed in this repository, at each step utilising a
new concept from git to make progress. We will present concepts first as theory before
then applying them to the codebase in practice.

With regards to specific content we cover:

* A deeper understanding of how git functions under the hood
* A quick recap of branching in git
* Use of patched commits and amending
* Use of git's stash feature
* Rebasing
* Merge conflicts and resolution
* Bisect to locate issue introduction points


## Teaching Material

### Slides

The slides for this workshop can be viewed here: [cambridge-iccs.github.io/intermediate-git](https://cambridge-iccs.github.io/intermediate-git).

They are written in quarto markdown, rendered to reveal.js, and can be found in the
`slides` directory.

### Exercises

The exercises for the course can be found in the slides.  
They take the form of practical application of the git features introduced in the
slides to the enclosed `thermolib` library.
This is a simple Python library providing basic implementation of some thermodynamic
equations in atmospheric science.


## Preparation and prerequisites

### Prerequisites

To get the most out of the session we assume a basic understanding in a few areas and 
for you to do some preparation in advance.
This expected knowledge is outlined below, along with resources for reading if you
are unfamiliar with any areas.

- We assume users are familiar with basic use of git. Commands such as `add`, `commit`,
  `push`, `pull`, and have a basic knowledge of creating branches.
    - If these are unfamiliar we suggest attending or reviewing the ICCS
      introduction to git [repository](https://github.com/Cambridge-ICCS/Summer-school-Intro-Git)
      and [recording](https://www.youtube.com/watch?v=dP4wljuajho).
- The exercises will make use of a Python codebase, but no specialised knowledge is required.
    - We assume users are familiar with the basics of Python, modular code, writing
      functions, and running scripts.

### Preparation

To participate in this session you will need a few basic things installed on your
computer:

- A text editor - e.g. vim/[neovim](https://neovim.io/), [gedit](https://gedit.en.softonic.com/),
  [VSCode](https://code.visualstudio.com/), [sublimetext](https://www.sublimetext.com/) etc.
  to open and edit code files,
- A terminal emulator - e.g. [GNOME Terminal](https://help.gnome.org/users/gnome-terminal/stable/),
  [wezterm](https://wezfurlong.org/wezterm/index.html),
  [Windows Terminal (windows only)](https://learn.microsoft.com/en-us/windows/terminal/),
  [iTerm (Mac only)](https://iterm2.com/) to run git commands and execute code,
- git 
    - This should come as standard on linux and MacOS and can be installed on Windows.
      For details on checking that git is installed, and obtaining it if not,
      see the [git Getting Started documentation](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
- A Python 3 installation
    - This should come as standard on linux and can be installed on mac and Windows
      (see notes below).
    - We will use `pip` for installing Python packages.
      Often this will come with Python, but some operating systems/distributions disable it.
      If `pip` is not available on the command line you can add it to a virtual environment
      using `python -m ensurepip --upgrade`

> [!NOTE]
> For MacOS users: Python 3 can be installed through several popular package managers.
> Alternatively, if you are unfamiliar with this, refer to
> [Python's getting-started on mac information](https://docs.python.org/3/using/mac.html)
> for a complete guide to getting set up.

> [!NOTE]
> For Windows users: we recommend using the [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install)
> for an experience as close as possible to the workshop demonstration.
> If this is not possible you may wish to refer to
> [Windows' getting-started with Python information](https://learn.microsoft.com/en-us/windows/python/beginners)
> for a complete guide to getting set up on a Windows system.

If you require assistance or further information with any of these please reach out to
us before the session.


## Installation and setup

### Obtaining the materials

In preparation for the course you should clone a copy of this repository to your machine
to work on.

Navigate to the location you want to place the files and clone via https by running:
```sh
git clone https://github.com/Cambridge-ICCS/intermediate-git.git
```
This will create a directory `intermediate-git/` with the contents of this repository.

Please note that if you have a GitHub account and want to preserve any work you do
we suggest you first [fork the repository](https://github.com/Cambridge-ICCS/intermediate-git/fork) 
and then clone your fork.
This will allow you to push your changes and progress from the workshop back up to your
fork for future reference.

### Installation into a virtual environment

The code we will be working with in the exercises is a simple Python library 
You can then instantiate a Python virtual environment by running:
```sh
python3 -m venv int-git-venv
```
This will create a directory called `int-git-venv` containing software for the virtual environment.
To activate the environment run:
```sh
source int-git-venv/bin/activate
```
You can now work on Python from within this isolated environment, installing packages
as you wish without disturbing your base system environment.

To install the `thermolib` library run:
```sh
pip install --editable .
```
This will add `thermolib` into the environment.
By using the `--editable` flag any changes we make to the code will be immediately
reflected rather than requiring reinstallation of the library.

When you have finished working on this project run:
```sh
deactivate
```
to deactivate the virtual environment and return to the system Python.

You can always boot back into the venv as you left it by running the activate command again.


## License

The code materials in this project are licensed under an [MIT License](LICENSE).

The teaching materials are licensed under a separate
Creative Commons License [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).


## Contribution Guidelines and Support

If you spot an issue with the materials please let us know by
[opening an issue](https://github.com/Cambridge-ICCS/intermediate-git/issues)
here on GitHub clearly describing the problem.

If you are able to fix an issue that you spot, or an
[existing open issue](https://github.com/Cambridge-ICCS/intermediate-git/issues)
please get in touch by commenting on the issue thread.

Contributions from the community are welcome.
To contribute back to the repository please first
[fork it](https://github.com/Cambridge-ICCS/intermediate-git/fork),
make the necessary changes to fix the problem, and then open a pull request back to
this repository clearly describing the changes you have made.
We will then preform a review and merge once ready.

If you would like support using these materials, adapting them to your needs, or
have them delivered as a training workshop please get in touch either via GitHub or via
[ICCS](https://github.com/Cambridge-ICCS).
