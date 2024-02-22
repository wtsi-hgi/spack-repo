# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparsegam(RPackage):
	"""Sparse Generalized Additive Models

	Fits sparse frequentist GAMs (SF-GAM) for continuous and discrete responses in the exponential dispersion family with the group lasso, group smoothly clipped absolute deviation (SCAD), and group minimax concave (MCP) penalties <doi:10.1007/s11222-013-9424-2>. Also fits sparse Bayesian generalized additive models (SB-GAM) with the spike-and-slab group lasso (SSGL) penalty of Bai et al. (2021) <doi:10.1080/01621459.2020.1765784>. B-spline basis functions are used to model the sparse additive functions. Stand-alone functions for group-regularized negative binomial regression, group-regularized gamma regression, and group-regularized regression in the exponential dispersion family with the SSGL penalty are also provided.
	"""
	
	cran = "sparseGAM" 

	version("1.0", md5="676704e9bf71869149924aecde86cab3")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-grpreg", type=("build", "run"))
