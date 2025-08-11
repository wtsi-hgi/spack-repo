# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFunctools32(PythonPackage):
    """This is a backport of the Python 3.2 functools module for use on Python versions 2.7 and PyPy. It includes new features lru_cache (Least-recently-used cache decorator)."""

    homepage = "https://github.com/MiCHiLU/python-functools32"
    pypi = "functools32/functools32-3.2.3-2.tar.gz"

    version("3.2.3-2", sha256="f6253dfbe0538ad2e387bd8fdfd9293c925d63553f5813c4e587745416501e6d")

    depends_on("python@2", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    def patch(self):
        filter_file("from distutils.core import setup", "from setuptools import setup", "setup.py", string=True)
