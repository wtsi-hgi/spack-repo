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
#     spack install py-blobtools
#
# You can edit this file again by typing:
#
#     spack edit py-blobtools
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyBlobtools(PythonPackage):
    """A modular command-line solution for visualisation, quality control and taxonomic partitioning of genome datasets."""

    homepage = "https://github.com/DRL/blobtools"
    url = "https://github.com/DRL/blobtools/archive/refs/tags/blobtools_v1.1.1.tar.gz"
    git = "https://github.com/DRL/blobtools.git"

    license("GPL-3.0")
    version(
        "20240821",
        commit="9426ca4a6dd0e0a2a67841d92b60b101fc52b921",
    )

    depends_on("py-setuptools", type="build")
    depends_on("py-matplotlib")
    depends_on("py-docopt")
    depends_on("py-tqdm")
    depends_on("wget")
    depends_on("py-pyyaml")
    depends_on("py-pysam")
