# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyZstandard(PythonPackage):
    """This project provides Python bindings for interfacing with the Zstandard compression library. A C extension and CFFI interface are provided."""

    homepage = "https://github.com/indygreg/python-zstandard"
    pypi = "zstandard/zstandard-0.22.0.tar.gz"

    version("0.22.0", sha256="8226a33c542bcb54cd6bd0a366067b610b41713b64c9abec1bc4533d69f51e70")

    depends_on("py-cffi@1.11:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
