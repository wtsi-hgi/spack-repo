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
#     spack install py-pbcoretools
#
# You can edit this file again by typing:
#
#     spack edit py-pbcoretools
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyPbcoretools(PythonPackage):
    """The pbcoretools package provides Python CLIs for interacting with PacBio data files
    and writing bioinformatics applications. Main components are:

    1. the dataset command, for all dataset XML operations
    2. the bamsieve command, for advanced BAM/dataset subsetting
    3. SMRT Link analysis application tasks
    """

    homepage = "https://web.archive.org/web/20201227035306/https://github.com/PacificBiosciences/pbcoretools"
    url = "https://web.archive.org/web/20201227035410if_/https://codeload.github.com/PacificBiosciences/pbcoretools/tar.gz/0.8.1"

    version("0.8.1", sha256="d48c4a15659adfa1c53db84cf73a4f1707d27765aa0eef326f734ed369c1ac8a", extension="tar.gz")

    license("BSD-3-Clause-Clear license")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-numpy@1.17:1.22.4", type=("build", "run"))
    depends_on("py-pysam@0.15.1:", type=("build", "run"))
    depends_on("py-pbcore", type=("build", "run"))
    depends_on("py-pbcommand", type=("build", "run"))
    depends_on("py-setuptools", type=("build", "run"))
