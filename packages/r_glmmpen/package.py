# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmmpen(RPackage):
	"""High Dimensional Penalized Generalized Linear Mixed Models
(pGLMM)

	Fits high dimensional penalized generalized linear 
    mixed models using 
    the Monte Carlo Expectation Conditional Minimization (MCECM) algorithm. 
    The purpose of the package is to perform variable selection on both the fixed and 
    random effects simultaneously for generalized linear mixed models.
    The package supports fitting of Binomial, Gaussian, and Poisson data with canonical links, and
    supports penalization using the MCP, SCAD, or LASSO penalties. The MCECM algorithm
    is described in Rashid et al. (2020) <doi:10.1080/01621459.2019.1671197>.
    The techniques used in the minimization portion of the procedure (the M-step) are
    derived from the procedures of the 'ncvreg' package (Breheny and Huang (2011) 
    <doi:10.1214/10-AOAS388>) and 'grpreg' package (Breheny and Huang (2015)
    <doi:10.1007/s11222-013-9424-2>), with
    appropriate modifications to account for the estimation and penalization of
    the random effects. The 'ncvreg' and 'grpreg' packages also describe the MCP, SCAD, 
    and LASSO penalties.
	"""
	
	cran = "glmmPen" 

	version("1.5.4.4", md5="da1d602193d54077a88b2da0c48b1760")

	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-bigmemory", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ncvreg", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rstantools", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
