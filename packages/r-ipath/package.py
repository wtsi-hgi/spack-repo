# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpath(RPackage):
	"""iPath pipeline for detecting perturbed pathways at individual level

	iPath is the Bioconductor package used for calculating personalized pathway score and test the association with survival outcomes. Abundant single-gene biomarkers have been identified and used in the clinics. However, hundreds of oncogenes or tumor-suppressor genes are involved during the process of tumorigenesis. We believe individual-level expression patterns of pre-defined pathways or gene sets are better biomarkers than single genes. In this study, we devised a computational method named iPath to identify prognostic biomarker pathways, one sample at a time. To test its utility, we conducted a pan-cancer analysis across 14 cancer types from The Cancer Genome Atlas and demonstrated that iPath is capable of identifying highly predictive biomarkers for clinical outcomes, including overall survival, tumor subtypes, and tumor stage classifications. We found that pathway-based biomarkers are more robust and effective than single genes.
	"""
	
	bioc = "iPath" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/iPath_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/iPath/iPath_1.8.0.tar.gz"]

	version("1.8.0", sha256="53c8c92e77d5a26987fbc2d0eafb479d02f0fd563b6e72a4fb00ffc749a05326")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-survminer", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
