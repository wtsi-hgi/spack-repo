# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsgl(RPackage):
	"""Spike-and-Slab Group Lasso for Group-Regularized Generalized
Linear Models

	Fits group-regularized generalized linear models (GLMs) using the spike-and-slab group lasso (SSGL) prior introduced by Bai et al. (2022) <doi:10.1080/01621459.2020.1765784> and extended to GLMs by Bai (2023) <arXiv:2007.07021>. This package supports fitting the SSGL model for the following GLMs with group sparsity: Gaussian linear regression, binary logistic regression, Poisson regression, negative binomial regression, and gamma regression.
 Stand-alone functions for group-regularized negative binomial regression and group-regularized gamma regression are also available, with the option of employing the group lasso penalty of Yuan and Lin (2006) <doi:10.1111/j.1467-9868.2005.00532.x>, the group minimax concave penalty (MCP) of Breheny and Huang <doi:10.1007/s11222-013-9424-2>, or the group smoothly clipped absolute deviation (SCAD) penalty of Breheny and Huang (2015) <doi:10.1007/s11222-013-9424-2>.
	"""
	
	cran = "SSGL" 

	version("1.0", md5="eaf1336a94221ef43ebcfc2439776b62")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-grpreg", type=("build", "run"))
