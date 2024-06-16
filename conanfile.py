#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conan import ConanFile
from conan.errors import ConanInvalidConfiguration
from conan.tools.files import download, copy
import json, os

required_conan_version = ">=2.0"

class QtIFConan(ConanFile):

    jsonInfo = json.load(open("info.json", 'r'))
    # ---Package reference---
    name = jsonInfo["projectName"]
    version = jsonInfo["version"]
    user = jsonInfo["domain"]
    channel = "stable"
    # ---Metadata---
    description = jsonInfo["projectDescription"]
    license = jsonInfo["license"]
    author = jsonInfo["vendor"]
    topics = jsonInfo["topics"]
    homepage = jsonInfo["homepage"]
    url = jsonInfo["repository"]
    # ---Requirements---
    requires = []
    tool_requires = []
    # ---Sources---
    exports = ["info.json"]
    exports_sources = []
    # ---Binary model---
    settings = "os", "arch"
    options = {}
    default_options = {}
    # ---Build---
    generators = []
    # ---Folders---
    no_copy_source = True

    @property
    def installer_name(self):
        if self.settings.os == "Linux":
            return "QtInstallerFramework-linux-x64-%s.run" % self.version
        elif self.settings.os == "Windows":
            return "QtInstallerFramework-windows-x64-%s.exe" % self.version

    @property
    def installer_cmd(self):
        if self.settings.os == "Linux":
            return "./%s" % self.installer_name
        elif self.settings.os == "Windows":
            return self.installer_name

    def system_requirements(self):
        if self.settings.os == "Linux":
            apt = Apt(self)
            pack_names = ["libgl1-mesa-dev", "libfontconfig1-dev", "libfreetype6-dev", "libx11-dev", "libx11-xcb-dev", "libxext-dev", "libxfixes-dev", "libxi-dev", "libxrender-dev", "libxcb1-dev", "libxcb-cursor-dev", "libxcb-glx0-dev", "libxcb-keysyms1-dev", "libxcb-image0-dev", "libxcb-shm0-dev", "libxcb-icccm4-dev", "libxcb-sync-dev", "libxcb-xfixes0-dev", "libxcb-shape0-dev", "libxcb-randr0-dev", "libxcb-render-util0-dev", "libxcb-util-dev", "libxcb-xinerama0-dev", "libxcb-xkb-dev", "libxkbcommon-dev", "libxkbcommon-x11-dev"]
            apt.install(pack_names, update=True)

    def validate(self):
        valid_os = ["Windows", "Linux"]
        if str(self.settings.os) not in valid_os:
            raise ConanInvalidConfiguration(f"Qt Installer Framework {self.version} is only supported for the following operating systems: {valid_os}")
        valid_arch = ["x86_64"]
        if str(self.settings.arch) not in valid_arch:
            raise ConanInvalidConfiguration(f"Qt Installer Framework {self.version} is only supported for the following architectures on {self.settings.os}: {valid_arch}")

    def build(self):
        source_url = "https://download.qt.io/official_releases/qt-installer-framework/%s/%s" % (self.version, self.installer_name)
        download(self, source_url, filename=self.installer_name)
        if self.settings.os == "Linux":
            self.run("chmod +x " + self.installer_name)
        self.run("%s in --al -c --cp %s -t %s" % (self.installer_cmd, self.build_folder , self.package_folder))

    def package_info(self):
        self.output.info('Prepending to PATH environment variable: %s' % self.package_folder)
        self.buildenv_info.prepend_path("PATH", os.path.join(self.package_folder, "bin"))
