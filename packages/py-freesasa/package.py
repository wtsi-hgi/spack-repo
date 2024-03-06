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

    # FIXME: Only add the python/pip/wheel dependencies if you need specific versions
    # or need to change the dependency type. Generic python/pip/wheel dependencies are
    # added implicity by the PythonPackage base class.
    # depends_on("python@2.X:2.Y,3.Z:", type=("build", "run"))
    # depends_on("py-pip@X.Y:", type="build")
    # depends_on("py-wheel@X.Y:", type="build")

    # FIXME: Add a build backend, usually defined in pyproject.toml. If no such file
    # exists, use setuptools.
    depends_on("py-setuptools", type="build")
    # depends_on("py-hatchling", type="build")
    # depends_on("py-flit-core", type="build")
    # depends_on("py-poetry-core", type="build")

    # FIXME: Add additional dependencies if required.
    #depends_on("py-foo", type=("build", "run"))
    depends_on("freesasa", type=("build", "run"))
