# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNnmis(RPackage):
	"""Nearest Neighbor Based Multiple Imputation for Survival Data
with Missing Covariates

	Imputation for both missing covariates and censored observations (optional) for survival data with missing covariates by the nearest neighbor based multiple imputation algorithm as described in Hsu et al. (2006) <doi:10.1002/sim.2452>, and Hsu and Yu (2018) <doi: 10.1177/0962280218772592>. Note that the current version can only impute for a situation with one missing covariate.
	"""
	
	cran = "NNMIS" 

	version("1.0.1", md5="99abc7de3654ab7d1b19313312903731")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
