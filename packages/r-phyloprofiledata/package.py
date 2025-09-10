# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhyloprofiledata(RPackage):
    """Data package for phylogenetic profile analysis using PhyloProfile tool

    Two experimental datasets to illustrate running and analysing phylogenetic profiles with PhyloProfile package.
    """

    homepage = "https://github.com/BIONF/PhyloProfileData"
    bioc = "PhyloProfileData"

    version("1.22.3", commit="4b50e3eccb5645ae1c42a6b1b1fb562b7d56897d")
    version("1.16.0", commit="a7660cf16daa3b3e6c8639c3d09c595f6aaff63a")

    # PhyloProfileData 1.22.3 requires R >= 4.5 (fails with 4.4.x)
    # depends_on("r@4.5:", type=("build", "run"))
    depends_on("r-experimenthub", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-biocstyle", type=("build", "run"))
