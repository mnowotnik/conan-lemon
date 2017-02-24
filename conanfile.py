from conans import ConanFile
import os
from os import path
from conans.tools import download, unzip, check_sha256
from conans import CMake

LEMON_COMMIT = '5ccba178a8e8a4b21e1c9232944d23973da38ad7'
LEMPAR_COMMIT = 'db1bdb4821f2d8fbd76e577cf3ab18642c8d08d1'

LEMON_C_URL_TMPL = 'http://www.sqlite.org/src/raw/tool/lemon.c?name={}'
LEMPAR_C_URL_TMPL = 'http://www.sqlite.org/src/raw/tool/lempar.c?name={}'

LEMON_C_SHA = '${lemon_c_sha}'
LEMPAR_C_SHA = '${lempar_c_sha}'

LEMON_C_URL = LEMON_C_URL_TMPL.format(LEMON_COMMIT)
LEMPAR_C_URL = LEMPAR_C_URL_TMPL.format(LEMPAR_COMMIT)


class LemonConanFile(ConanFile):
    name = "lemon"
    version = "master"
    license = "Public Domain"
    generators = "cmake"
    url = "http://github.com/Mike-Now/conan-lemon"

    def source(self):
        download(LEMON_C_URL, 'lemon.c')
        download(LEMPAR_C_URL, 'lempar.c')
        # check_sha256(zip_name, self.FILE_SHA)
        # unzip(zip_name)
        # os.unlink(zip_name)

    def package(self):
        self.copy('lemon.c', dst='include')
        self.copy('lempar.c', dst='include')
