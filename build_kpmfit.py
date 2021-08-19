# -*- coding: utf-8 -*-
import logging
import numpy
logging.basicConfig(level=logging.DEBUG)

from distutils.core import setup
from distutils.extension import Extension

from Cython.Distutils import build_ext
import Cython.Compiler.Options
Cython.Compiler.Options.annotate = False

setup(
    cmdclass = {'build_ext': build_ext},
    include_dirs=[numpy.get_include()],
    ext_modules = [Extension("_kmpfit", sources=["src/kmpfit.pyx", "src/mpfit.c"])],
    script_args = ['build_ext', '--inplace']
)