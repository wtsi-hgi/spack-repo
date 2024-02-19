# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyScallele(PythonPackage):
    """scAllele is a versatile tool to detect and analyze nucleotide variants in scRNA-seq."""

    homepage = "https://www.example.com"
    pypi = "scAllele/scAllele-0.0.9.3.tar.gz"

    version("0.0.9.3", sha256="fe0c3d8c1a4dadea52d04d64d319224edd87189195b2767b2ed9c441b16e3b3c")

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
    # depends_on("py-foo", type=("build", "run"))
