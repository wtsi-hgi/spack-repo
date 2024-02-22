# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMrmlmGui(RPackage):
	"""Multi-Locus Random-SNP-Effect Mixed Linear Model Tools for
Genome-Wide Association Study with Graphical User Interface

	Conduct multi-locus genome-wide association study under the framework of multi-locus random-SNP-effect mixed linear model (mrMLM). First, each marker on the genome is scanned. Bonferroni correction is replaced by a less stringent selection criterion for significant test. Then, all the markers that are potentially associated with the trait are included in a multi-locus genetic model, their effects are estimated by empirical Bayes and all the nonzero effects were further identified by likelihood ratio test for true QTL. Wen YJ, Zhang H, Ni YL, Huang B, Zhang J, Feng JY, Wang SB, Dunwell JM, Zhang YM, Wu R (2018) <doi:10.1093/bib/bbw145>.
	"""
	
	cran = "mrMLM.GUI" 

	version("4.0.2", md5="8e46c8757878bcdf711370b4af3a00e4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-lars", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ncvreg", type=("build", "run"))
	depends_on("r-coin", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-sampling", type=("build", "run"))
	depends_on("r-bigmemory", type=("build", "run"))
	depends_on("r-mrmlm", type=("build", "run"))
	depends_on("r-sbl", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
