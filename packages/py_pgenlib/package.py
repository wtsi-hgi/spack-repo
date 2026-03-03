# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPgenlib(PythonPackage):
    """This provides a basic Python API for pgenlib."""

    homepage = "https://github.com/chrchang/plink-ng"
    pypi = "Pgenlib/Pgenlib-0.90.1.tar.gz"

    version("0.90.1", sha256="069db673c1cc5baffcb9b20c2e6e26cc9fdaadd0095f55a188b41502d0511cb9")

    depends_on("py-setuptools", type="build")
    depends_on("py-cython@0.29.21:", type=("build", "run"))
    depends_on("py-numpy@1.19.0:", type=("build", "run"))
    depends_on("zlib", type=("build", "link"))
