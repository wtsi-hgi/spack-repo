# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClstutils(RPackage):
    """Tools for performing taxonomic assignment

    Tools for performing taxonomic assignment based on phylogeny using pplacer and clst.
    """

    bioc = "clstutils"

    version("1.56.0", commit="9c5813f495a87f19460b5ea93dbe5b98856ed75a")
    version("1.50.0", commit="51194cc00de93fa546d766e2bddc2702d417cd04")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-clst", type=("build", "run"))
    depends_on("r-rjson", type=("build", "run"))
    depends_on("r-ape", type=("build", "run"))
    depends_on("r-lattice", type=("build", "run"))
    depends_on("r-rsqlite", type=("build", "run"))
