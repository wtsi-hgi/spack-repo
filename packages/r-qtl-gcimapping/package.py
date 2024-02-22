# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQtlGcimapping(RPackage):
	"""QTL Genome-Wide Composite Interval Mapping

	Conduct multiple quantitative trait loci (QTL) and QTL-by-environment interaction (QEI) mapping via ordinary or compressed variance component mixed models with random- or fixed QTL/QEI effects. First, each position on the genome is detected in order to obtain a negative logarithm P-value curve against genome position. Then, all the peaks on each effect (additive or dominant) curve or on each locus curve are viewed as potential main-effect QTLs and QEIs, all their effects are included in a multi-locus model, their effects are estimated by both least angle regression and empirical Bayes (or adaptive lasso) in backcross and F2 populations, and true QTLs and QEIs are identified by likelihood radio test. See Zhou et al. (2022) <doi:10.1093/bib/bbab596> and Wen et al. (2018) <doi:10.1093/bib/bby058>.
	"""
	
	cran = "QTL.gCIMapping" 

	version("3.4", md5="9d0e312243f0709a81cd06e84b97abb5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-lars", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-qtl", type=("build", "run"))
