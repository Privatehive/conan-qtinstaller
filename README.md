# conan-qtinstaller

[![Conan Remote Recipe](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.github.com%2Frepos%2FPrivatehive%2Fconan-qtinstaller%2Fproperties%2Fvalues&query=%24%5B0%5D.value&style=flat&logo=conan&label=conan&color=%232980b9)](https://conan.privatehive.de/ui/repos/tree/General/public-conan/de.privatehive/qtinstaller) 

#### A conan package that provides the Qt installer framework

---

| os        | arch     | CI Status                                                                                                                                                                                                                                                                 |
| --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Linux`   | `x86_64` | [![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/Privatehive/conan-qtinstaller/main.yml?branch=master&style=flat&logo=github&label=create+package)](https://github.com/Privatehive/conan-qtinstaller/actions?query=branch%3Amaster) |
| `Windows` | `x86_64` | [![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/Privatehive/conan-qtinstaller/main.yml?branch=master&style=flat&logo=github&label=create+package)](https://github.com/Privatehive/conan-qtinstaller/actions?query=branch%3Amaster) |

### Usage

This package contains the binaries of the Qt installer framework to use in your recipe as a build dependency.

* The binaries for Windows: `archivegen.exe`, `binarycreator.exe`, `devtool.exe`, `repogen.exe`
* The binaries for Linux: `archivegen`, `binarycreator`, `devtool`, `repogen`
