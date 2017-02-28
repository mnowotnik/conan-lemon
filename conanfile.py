import os

from conans import CMake, ConanFile
from conans.tools import check_sha256, download

LEMON_COMMIT = '5ccba178a8e8a4b21e1c9232944d23973da38ad7'
LEMON_C_URL_TMPL = 'http://www.sqlite.org/src/raw/tool/lemon.c?name={}'
LEMON_C_SHA = 'cfe445840e2c484a95e7bb833a29eb1f827f72245050a630d224abeff7377387'
LEMON_C_URL = LEMON_C_URL_TMPL.format(LEMON_COMMIT)

LEMPAR_COMMIT = 'db1bdb4821f2d8fbd76e577cf3ab18642c8d08d1'
LEMPAR_C_URL_TMPL = 'http://www.sqlite.org/src/raw/tool/lempar.c?name={}'
LEMPAR_C_SHA = 'db176c73c3afc022d3075753ac14b9c753b57e770f9a3c09346a8615a51220ee'
LEMPAR_C_URL = LEMPAR_C_URL_TMPL.format(LEMPAR_COMMIT)


class LemonConanFile(ConanFile):
    name = 'lemon'
    author = 'D. Richard Hipp'
    version = 'master'
    license = 'Public Domain'
    settings = 'os', 'arch', 'compiler'
    url = 'http://github.com/Mike-Now/conan-lemon'
    description = 'Fast LALR(1) parser generator for C and C++'
    exports = 'CMakeLists.txt'
    generators = 'cmake'

    def source(self):
        download(LEMON_C_URL, 'lemon.c')
        download(LEMPAR_C_URL, 'lempar.c')
        check_sha256('lemon.c', LEMON_C_SHA)
        check_sha256('lempar.c', LEMPAR_C_SHA)

    def build(self):
        cmake = CMake(self.settings)
        self.run('mkdir build_')
        cmd = 'cd build_ && cmake .. {}'.format(cmake.command_line)
        self.output.warn(cmd)
        self.run(cmd)
        cmd = 'cd build_ && cmake --build . {}'.format(cmake.build_config)
        self.output.warn(cmd)
        self.run(cmd)

    def package(self):
        self.copy('lemon', dst='bin', src='build_')
        self.copy('lempar.c', dst='bin', src='')

    def package_info(self):
        self.env_info.path.append(os.path.join(self.package_folder, 'bin'))
