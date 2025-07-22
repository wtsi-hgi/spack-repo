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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/SBGNview.data_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/SBGNview.data/SBGNview.data_1.16.0.tar.gz"]

	version("1.16.0", sha256="d9c9737a624c60ebc3de0e5195a60d48e3001b8ea7e38a3c9749c599cf83f9da")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-bookdown", type=("build", "run"))

