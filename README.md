# Choice Project Manager

# Table of Contents
* [About](#about)
* [Installation](#installation)
* [How To Use](#how-to-use)
* [Version History](#version-history)
* [To-do](#to-do)

# About
v0.1.0

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

# How To Use

### Set your template directory
Go to the directory where all of your jinja2 templates will be stored

```
chpm -s
```

```
chpm set
```

The repository will come with a sample template folder as reference.

NOTE: Template folders must be the name of the language you wish to make the project of

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
- First working version
    - Can create new projects with project config
    - Can create new files with project config

# To-do

- [ ] Implement git features
    - [ ] Initialize repo
    - [ ] Add origin to remote repo
- [ ] Editing project config and applying changes across all files in the project
- [ ] Initializing project even if it has already been made but not using the project manager
- [ ] Have the script read from script env file to get list of template folders and not rely on language names
