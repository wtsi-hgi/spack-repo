# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMmhash3(PythonPackage):
    """mmhash3 is a Python wrapper for MurmurHash (MurmurHash3), a set of fast and robust non-cryptographic hash functions invented by Austin Appleby."""

    homepage = "https://github.com/Fokko/mmhash3"
    pypi = "mmhash3/mmhash3-3.0.1.tar.gz"

    version("3.0.1", sha256="a00d68f4a1cc434b9501513c8a29e18ed1ddad383677d72b41d71d0d862348af")

    depends_on("py-setuptools", type="build")
