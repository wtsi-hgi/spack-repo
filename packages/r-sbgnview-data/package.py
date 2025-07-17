# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSbgnviewData(RPackage):
    """Supporting datasets for SBGNview package

    This package contains: 1. A microarray gene expression dataset from a human breast cancer study. 2. A RNA-Seq gene expression dataset from a mouse study on IFNG knockout. 3. ID mapping tables between gene IDs and SBGN-ML file glyph IDs. 4. Percent of orthologs detected in other species of the genes in a pathway. Cutoffs of this percentage for defining if a pathway exists in another species. 5. XML text of SBGN-ML files for all pre-collected pathways.
    """

    bioc = "SBGNview.data"

    version("1.22.0", commit="3bea9d88411874cbecd16b1c732dfb10b92b5677")
    version("1.16.0", commit="2f6544fdea729d9f787a3e79d0a4c9523824f8aa")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))
    depends_on("r-bookdown", type=("build", "run"))
