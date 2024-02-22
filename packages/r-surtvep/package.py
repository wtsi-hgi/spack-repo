# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurtvep(RPackage):
	"""Cox Non-Proportional Hazards Model with Time-Varying
Coefficients

	Fit Cox non-proportional hazards models with time-varying coefficients. 
    Both unpenalized procedures (Newton and proximal Newton) and penalized procedures 
    (P-splines and smoothing splines) are included using B-spline basis functions for 
    estimating time-varying coefficients. For penalized procedures, cross validations, 
    mAIC, TIC or GIC are implemented to select tuning parameters. Utilities for 
    carrying out post-estimation visualization, summarization, point-wise confidence 
    interval and hypothesis testing are also provided.
    For more information, see Wu et al. (2022) <doi: 10.1007/s10985-021-09544-2> and 
    Luo et al. (2023) <doi:10.1177/09622802231181471>.
	"""
	
	homepage = "https://github.com/UM-KevinHe/surtvep"
	cran = "surtvep" 

	version("1.0.0", md5="5e0376172d2998e64cccb69ade3aabeb")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
