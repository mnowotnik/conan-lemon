from conans.model.conan_file import ConanFile
from conans import CMake
import os

default_user = "MikeNow"
default_channel = "stable"

channel = os.getenv("CONAN_CHANNEL", default_channel)
username = os.getenv("CONAN_USERNAME", default_user)

class DefaultNameConan(ConanFile):
    name = "DefaultName"
    version = "0.1"
    settings = "os", "compiler", "arch", "build_type"
    generators = "cmake"
    requires = "lemon/master@%s/%s" % (username, channel)

    def build(self):
        cmake = CMake(self.settings)
        self.output.warn('cmake {} {}'.format(self.conanfile_directory, cmake.command_line))
        self.run('cmake {} {}'.format(self.conanfile_directory, cmake.command_line))
        self.output.warn('cmake --build ../.. --target gen {}'.format(cmake.build_config))
        self.run('cmake --build {} --target gen {}'.format(self.conanfile_directory, cmake.build_config))
        
    def test(self):
        self.run("ls {}/test.out".format(self.conanfile_directory))
