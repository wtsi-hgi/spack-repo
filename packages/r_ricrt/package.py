# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRicrt(RPackage):
	"""Randomization Inference of Clustered Randomized Trials

	Methods for randomization inference in group-randomized trials. Specifically, it can be used to analyze the treatment effect of stratified data with multiple clusters in each stratum with treatment given on cluster level. 
    User may also input as many covariates as they want to fit the data. Methods are described by Dylan S Small et al., (2012) <doi:10.1198/016214507000000897>.
	"""
	
	cran = "Ricrt" 

	version("0.1.0", md5="e84bcb8198bee9ff047fa821ff9d9cd6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-superlearner", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
