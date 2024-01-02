# Choice Project Manager

[![version](https://img.shields.io/badge/version-0.1.1-blue.svg)](https://github.com/choisauce/choice-project-manager)
[![License](https://img.shields.io/badge/License-GPL3.0-red.svg)](https://github.com/choisauce/choice-project-manager/blob/main/LICENSE)

![Demo](./readme_assets/chpm.gif)

# Table of Contents
* [About](#about)
* [Installation](#installation)
* [How To Use](#how-to-use)
* [Version History](#version-history)
* [To-do](#to-do)

# About
[v0.1.2](##0.1.2)

A project template manager created using Jinja2 in python to create new project and add new files to projects created with this

Copyright &copy; 2023 Austin Choi

# Installation
The project is currently not available on pip and can only be installed using the following steps

1. Clone the project 
`git clone https://github.com/chosauce/choicePackageManager`

2. Run the dependencies script to download all the necessary dependencies

Windows

As of now, not planning on making work for windows sorry :(

Linux (NOTE: Need to check if the script contains all necessary pip packages to install lol)

```
./dependencies
```

Mac (NOTE: Might need to test if the dependencies script works for mac)

```
sudo chmod u+x ./dependencies
./dependencies
```

3. Run the build script to build the project

```
./build
```

# How To Use

### Set your template directory
Go to the directory where all of your jinja2 templates will be stored

```
chpm -s
```

```
chpm set
```

The repository will come with a sample template folder as a reference. You can use this template directory example as your primary template directory and change it how you wish.

NOTE: Template folders must be the name of the language you wish to make the project of. There must also be a newfile directory inside of the templates directory that has the templates of all the new files you can create for a language

Template directory structure
```
└── templates_directory
    ├── c
    ├── c#
    ├── c++
    ├── html
    ├── java
    ├── newfile
    │   ├── README.md
    │   ├── template.cpp
    │   ├── template.h
    │   ├── template.hpp
    │   ├── template.html
    │   ├── template.js
    │   ├── templateMain.cpp
    │   ├── template.py
    │   ├── template.sh
    │   └── template.ts
    ├── python
    └── ...
```

If you would like to add more languages that aren't currently supported, you can modify the `choice-project-manager/chpm/main.py` script and add the languages to the LANGUAGES array and update the ALL_LANGUAGES array if it wasn't listed there initially.

### Create projects

```
chpm create
```

Flags
- `-n, --name` - Project name
- `-d, --desc` - Project description
- `-a, --auth` - Project author

### Create new file in a Choice project

```
chpm newfile
```

Flags
- `-f, --newfile` - New file name


### Help

```
chpm --help
```

# Version History

## 0.1.0
- [x] First working version
    - [x] Can create new projects with project config
    - [x] Can create new files with project config

## 0.1.1
- [x] Implement git features
    - [x] Initialize repo
- [x] Getting list of template directories from the root template directory

## 0.1.2
- [x] Implemented dynamically getting template names from the template directory

# To-do

- [x] Implement git features
    - [x] Initialize repo
    - [ ] Add origin to remote repo
- [ ] Editing project config and applying changes across all files in the project
- [ ] Initializing project even if it has already been made but not using the project manager
- [x] Have the script read from script env file to get list of template folders and not rely on language names
    - [ ] Need to use this to get the prompt for what template to use
- [ ] Have project automatically add license in template
- [ ] Make it more user-friendly and usable by more people since this was originally made with myself in mind
- [ ] Create task management features
    - [ ] Progress tracking
    - [ ] Time tracking
- [ ] Potential collaboration features
    - [ ] Can potentially be used to work with communication tools like slack, discord, etc
