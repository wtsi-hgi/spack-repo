# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-paccmann-omics
#
# You can edit this file again by typing:
#
#     spack edit py-paccmann-omics
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyPaccmannOmics(PythonPackage):
    """Generative models of omic data for PaccMann."""

    homepage = "https://github.com/PaccMann/paccmann_omics/"

    url = "https://github.com/PaccMann/paccmann_omics/archive/refs/tags/0.0.1.1.tar.gz"

    license("MIT")

    version("0.0.2", sha256="a04ef89360376040ef9acf445c9cea31ba5069732d6ffd49db1a7c63ea4d69d2")
    version("0.0.1.1", sha256="1669589d46474892db0d69bb8a92024860abd12f8001c8181757f4202686c40d")

    depends_on("py-setuptools", type="build")
    depends_on("py-pytoda", type=("build", "run"))
    depends_on("py-absl-py", type=("build", "run"))
