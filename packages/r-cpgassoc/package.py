# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCpgassoc(RPackage):
	"""Association Between Methylation and a Phenotype of Interest

	Is designed to test for association between methylation at CpG sites across the genome and a phenotype of interest, adjusting for any relevant covariates. The package can perform standard analyses of large datasets very quickly with no need to impute the data. It can also handle mixed effects models with chip or batch entering the model as a random intercept. Also includes tools to apply quality control filters, perform permutation tests, and create QQ plots, manhattan plots, and scatterplots for individual CpG sites.	
	"""
	
	cran = "CpGassoc" 

	version("2.60", md5="668c3a5a22fb7e632319a4059f7fd5b2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
