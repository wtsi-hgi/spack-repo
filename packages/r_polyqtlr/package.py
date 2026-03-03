# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolyqtlr(RPackage):
	"""QTL Analysis in Autopolyploid Bi-Parental F1 Populations

	Quantitative trait loci (QTL) analysis and exploration of meiotic patterns in 
    autopolyploid bi-parental F1 populations. 
    For all ploidy levels, identity-by-descent (IBD) probabilities can be estimated.
    Significance thresholds, exploring QTL allele effects and visualising results are provided. 
    For more background and to reference the package see <doi:10.1093/bioinformatics/btab574>.
	"""
	
	cran = "polyqtlR" 

	version("0.1.1", md5="fa8cc6819a13accbeb327e4b7a6ac166")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
