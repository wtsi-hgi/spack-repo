# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsri(RPackage):
    """Gene Set Regulation Index

    The GSRI package estimates the number of differentially expressed genes in gene sets, utilizing the concept of the Gene Set Regulation Index (GSRI).
    """

    bioc = "GSRI"

    version("2.56.0", commit="3c14ff29fc10d7cf3f17228a30abefedd1671e55")
    version("2.50.0", commit="f0db687c08c572b57e06a4cc0173d2919a641469")

    depends_on("r@2.14.2:", type=("build", "run"))
    depends_on("r-fdrtool", type=("build", "run"))
    depends_on("r-genefilter", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-gseabase", type=("build", "run"))
    depends_on("r-les@1.1.6:", type=("build", "run"))
