# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMrmlm(RPackage):
	"""Multi-Locus Random-SNP-Effect Mixed Linear Model Tools for GWAS

	Conduct multi-locus genome-wide association study under the framework of multi-locus random-SNP-effect mixed linear model (mrMLM). First, each marker on the genome is scanned. Bonferroni correction is replaced by a less stringent selection criterion for significant test. Then, all the markers that are potentially associated with the trait are included in a multi-locus genetic model, their effects are estimated by empirical Bayes, and all the nonzero effects were further identified by likelihood ratio test for significant QTL. The program may run on a desktop or laptop computers. If marker genotypes in association mapping population are almost homozygous, these methods in this software are very effective. If there are many heterozygous marker genotypes, the IIIVmrMLM software is recommended. Wen YJ, Zhang H, Ni YL, Huang B, Zhang J, Feng JY, Wang SB, Dunwell JM, Zhang YM, Wu R (2018, <doi:10.1093/bib/bbw145>), and Li M, Zhang YW, Zhang ZC, Xiang Y, Liu MH, Zhou YH, Zuo JF, Zhang HQ, Chen Y, Zhang YM (2022, <doi:10.1016/j.molp.2022.02.012>).
	"""
	
	cran = "mrMLM" 

	version("5.0.1", md5="7f0a7be2098c444feb167f75546f4d08")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lars", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ncvreg", type=("build", "run"))
	depends_on("r-coin@1.1.0:", type=("build", "run"))
	depends_on("r-sampling", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-sbl", type=("build", "run"))
	depends_on("r-bedmatrix", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
