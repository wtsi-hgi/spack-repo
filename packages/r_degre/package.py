# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDegre(RPackage):
	"""Inferring Differentially Expressed Genes using Generalized
Linear Mixed Models

	Genes that are differentially expressed between two or more experimental conditions can be detected in RNA-Seq. A high biological variability may impact the discovery of these genes once it may be divergent between the fixed effects. However, this variability can be covered by the random effects. 'DEGRE' was designed to identify the differentially expressed genes considering fixed and random effects on individuals. These effects are identified earlier in the experimental design matrix. 'DEGRE' has the implementation of preprocessing procedures to clean the near zero gene reads in the count matrix, normalize by 'RLE' published in the 'DESeq2' package, 'Love et al. (2014)' <doi:10.1186/s13059-014-0550-8> and it fits a regression for each gene using the Generalized Linear Mixed Model with the negative binomial distribution, followed by a Wald test to assess the regression coefficients.
	"""
	
	cran = "DEGRE" 

	version("0.2.0", md5="1d734f23bf323fd377955e9d68ebd0d5")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-parglm", type=("build", "run"))
	depends_on("r-glmmtmb", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
