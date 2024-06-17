# conan-qtinstaller

### The Qt installer framework

[![Conan Badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2FTereius%2Fconan-qtinstaller%2Fmaster%2Finfo.json&query=%24.version&prefix=qtinstaller%2F&suffix=%40com.github.tereius%2Fstable&style=flat&logo=conan&label=conan&color=%232980b9)](https://conan.privatehive.de/ui/repos/tree/General/public-conan/com.github.tereius/qtinstaller)

| os | arch | Status |
|---|---|---|
| Linux | x86_64 | [![Build Status](https://dev.azure.com/bjoernstresing/bjoernstresing/_apis/build/status%2FTereius.conan-qtinstaller?repoName=Tereius%2Fconan-qtinstaller&branchName=master&jobName=Linux)](https://dev.azure.com/bjoernstresing/bjoernstresing/_build/latest?definitionId=30&repoName=Tereius%2Fconan-qtinstaller&branchName=master) |
| Windows | x86_64 | [![Build Status](https://dev.azure.com/bjoernstresing/bjoernstresing/_apis/build/status%2FTereius.conan-qtinstaller?repoName=Tereius%2Fconan-qtinstaller&branchName=master&jobName=Windows)](https://dev.azure.com/bjoernstresing/bjoernstresing/_build/latest?definitionId=30&repoName=Tereius%2Fconan-qtinstaller&branchName=master) |


### Usage

This package contains the binaries of the Qt installer framework to use in your recipe as a build dependency.

* The binaries for Windows: `archivegen.exe`, `binarycreator.exe`, `devtool.exe`, `repogen.exe`
* The binaries for Linux: `archivegen`, `binarycreator`, `devtool`, `repogen`
