# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFreesasa(PythonPackage):
    """This module provides bindings for the FreeSASA C library. See http://freesasa.github.io/python/ for documentation."""

    homepage = "http://freesasa.github.io/python/"
    pypi = "freesasa/freesasa-2.2.1.tar.gz"

    version("2.2.1", sha256="5630e65d619cf6a062028d7c6297afe8c5b18c677c75f1c32a0938399f4f6850")

    depends_on("py-setuptools", type="build")
    depends_on("py-twine", type=("build", "run"))
    depends_on("py-cython", type=("build", "run"))
    depends_on("py-biopython", type=("build", "run"))
    depends_on("py-nose", type=("build", "run"))
    depends_on("freesasa", type=("build", "run"))
