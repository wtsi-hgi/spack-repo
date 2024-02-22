# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMastr(RPackage):
	"""Markers Automated Screening Tool in R

	mastR is an R package designed for automated screening of signatures of interest for specific research questions. The package is developed for generating refined lists of signature genes from multiple group comparisons based on the results from edgeR and limma differential expression (DE) analysis workflow. It also takes into account the background noise of tissue-specificity, which is often ignored by other marker generation tools. This package is particularly useful for the identification of group markers in various biological and medical applications, including cancer research and developmental biology.
	"""
	
	homepage = "https://davislaboratory.github.io/mastR"
	bioc = "mastR" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/mastR_1.2.3.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/mastR/mastR_1.2.3.tar.gz"]

	version("1.2.3", md5="e3c3d512fc0082d6c51dab26088b79f7")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-msigdb", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-seuratobject", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
