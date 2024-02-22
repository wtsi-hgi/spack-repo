# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvsparse(RPackage):
	"""Survival Analysis with Sparse Longitudinal Covariates

	Survival analysis with sparse longitudinal covariates under right censoring scheme. Different hazards models are involved. Please cite the manuscripts corresponding to this package:  Sun, Z. et al. (2022) <doi:10.1007/s10985-022-09548-6>, Sun, Z. and Cao, H. (2023)  <arXiv:2310.15877> and Sun, D. et al. (2023) <arXiv:2308.15549>. 
	"""
	
	cran = "SurvSparse" 

	version("0.1", md5="de48437a41939d4418f100737b0d1222")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-gaussquad", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
