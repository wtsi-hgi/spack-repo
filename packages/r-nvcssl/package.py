# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNvcssl(RPackage):
	"""Nonparametric Varying Coefficient Spike-and-Slab Lasso

	Fits Bayesian regularized varying coefficient models with the Nonparametric Varying Coefficient Spike-and-Slab Lasso (NVC-SSL) introduced by Bai et al. (2023) <arXiv:1907.06477>. Functions to fit frequentist penalized varying coefficients are also provided, with the option of employing the group lasso penalty of Yuan and Lin (2006) <doi:10.1111/j.1467-9868.2005.00532.x>, the group minimax concave penalty (MCP) of Breheny and Huang <doi:10.1007/s11222-013-9424-2>, or the group smoothly clipped absolute deviation (SCAD) penalty of Breheny and Huang (2015) <doi:10.1007/s11222-013-9424-2>.
	"""
	
	cran = "NVCSSL" 

	version("2.0", md5="4da1e06aa0821f2495b69642aaf32862")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dae", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-gigrvg", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-grpreg", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
