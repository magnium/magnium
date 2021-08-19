#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy
from setuptools import setup, Extension
from Cython.Build import cythonize

requirements = ['numpy']

setup(
      name='kmpfit',
      use_scm_version=dict(version_scheme='{.tag}'.format, local_scheme=lambda vers: '.{}'.format(vers.distance or 0)),
      setup_requires=['setuptools_scm'],
      description='kmpfit library',
      long_description='',
      install_requires=requirements,
      include_dirs=[numpy.get_include()],
      packages=['kmpfit'],
      ext_modules = cythonize(Extension("_kmpfit", ["src/kmpfit.pyx", "src/mpfit.c"]), annotate=False),
      license = 'BSD',
      classifiers=[
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'Operating System :: Microsoft :: Windows',
      'Programming Language :: Python',
      'Topic :: Scientific/Engineering',
      'Topic :: Software Development :: Libraries',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
      'Programming Language :: Python :: 3.8',
      'Programming Language :: Python :: 3.9',
      ],
   )
