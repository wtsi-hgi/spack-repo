# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQtlGcimappingGui(RPackage):
	"""QTL Genome-Wide Composite Interval Mapping with Graphical User
Interface

	Conduct multiple quantitative trait loci (QTL) mapping under the framework of random-QTL-effect linear mixed model. First, each position on the genome is detected in order to obtain a negative logarithm P-value curve against genome position. Then, all the peaks on each effect (additive or dominant) curve are viewed as potential QTL, all the effects of the potential QTL are included in a multi-QTL model, their effects are estimated by empirical Bayes in doubled haploid population or by adaptive lasso in F2 population, and true QTL are identified by likelihood radio test. See Wen et al. (2018) <doi:10.1093/bib/bby058>.
	"""
	
	cran = "QTL.gCIMapping.GUI" 

	version("2.1.1", md5="031b2b033bebdf16af503f0e17dfffc7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-qtl", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-qtl-gcimapping", type=("build", "run"))
