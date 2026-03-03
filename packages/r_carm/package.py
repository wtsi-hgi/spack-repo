# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCarm(RPackage):
	"""Covariate-Adjusted Adaptive Randomization via
Mahalanobis-Distance

	In randomized controlled trial (RCT), balancing covariate is often one of the most important concern. CARM package provides functions to balance the covariates and generate allocation sequence by covariate-adjusted Adaptive Randomization via Mahalanobis-distance (ARM) for RCT. About what ARM is and how it works please see Y. Qin, Y. Li, W. Ma, H. Yang, and F. Hu (2022). "Adaptive randomization via Mahalanobis distance" Statistica Sinica. <doi:10.5705/ss.202020.0440>. In addition, the package is also suitable for the randomization process of multi-arm trials. For details, please see Yang H, Qin Y, Wang F, et al. (2023). "Balancing covariates in multi-arm trials via adaptive randomization" Computational Statistics & Data Analysis.<doi:10.1016/j.csda.2022.107642>.
	"""
	
	cran = "CARM" 

	version("1.1.0", md5="f42648e815eabb3d30c3c1a3973c42a0")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-arrangements", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
