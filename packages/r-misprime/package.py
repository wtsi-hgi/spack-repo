# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMisprime(RPackage):
	"""Partial Replacement Imputation Estimation for Missing Covariates

	Partial Replacement Imputation Estimation (PRIME) can overcome problems caused by missing covariates in additive partially linear model. PRIME conducts imputation and regression simultaneously with known and unknown model structure. More details can be referred to 
    Zishu Zhan, Xiangjie Li and Jingxiao Zhang. (2022) <arXiv:2205.14994>.
	"""
	
	cran = "misPRIME" 

	version("0.1.0", md5="d985b6e508a9fd6cf095ea576a9c1461")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
