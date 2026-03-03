# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlmmGwas(RPackage):
	"""Pipeline for GWAS Using MLMM

	Pipeline for Genome-Wide Association Study using Multi-Locus Mixed Model from Segura V, Vilhjálmsson BJ et al. (2012) <doi:10.1038/ng.2314>. The pipeline include detection of associated SNPs with MLMM, model selection by lowest eBIC and p-value threshold, estimation of the effects of the SNPs in the selected model and graphical functions.
	"""
	
	cran = "mlmm.gwas" 

	version("1.0.6", md5="6b9e413334fa7891ac104178eeddcde8")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-multcompview@0.1.7:", type=("build", "run"))
	depends_on("r-multcomp@1.4.8:", type=("build", "run"))
	depends_on("r-coxme@2.2.5:", type=("build", "run"))
	depends_on("r-sommer@3.2:", type=("build", "run"))
	depends_on("r-matrix@1.2.10:", type=("build", "run"))
