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
#     spack install py-pbcore
#
# You can edit this file again by typing:
#
#     spack edit py-pbcore
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyPbcore(PythonPackage):
    """
    The pbcore package provides Python modules for processing PacBio data files and building PacBio bioinformatics
    applications.
    """

    homepage = "http://pacificbiosciences.github.io/pbcore/"

    url = "https://github.com/PacificBiosciences/pbcore/archive/refs/tags/2.1.2.tar.gz"

    license("BSD-3-Clause-Clear license")

    version("2.1.2", sha256="aa156d62b97e3b0e5173487f0c9a95ed75e24e377b65e88929969d3ee0551b29")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-biopython@1.74:", type=("build", "run"))
    depends_on("py-numpy@1.17:1.22.4", type=("build", "run"))
    depends_on("py-pysam@0.15.1:", type=("build", "run"))
    depends_on("py-setuptools", type=("build", "run"))
