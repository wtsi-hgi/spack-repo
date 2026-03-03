# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRefreg(RPackage):
	"""Conditional Multivariate Reference Regions

	An R package for estimating conditional multivariate reference regions. 
    The reference region is non parametrically estimated using a kernel density estimator.
    Covariates effects on the multivariate response means vector and variance-covariance
    matrix, thus on the region shape, are estimated by flexible additive predictors. 
    Continuous covariates non linear effects might be estimated using penalized splines smoothers.
    Confidence intervals for the covariates estimated effects might be derived from
    bootstrap resampling. Kernel density bandwidth can be estimated with different methods, including
    a method that optimize the region coverage. Numerical, and graphical, summaries
    can be obtained by the user in order to evaluate reference region performance with real data.
    Full mathematical details can be found in <doi:10.1002/sim.9163> and <doi:10.1007/s00477-020-01901-1>.
	"""
	
	cran = "refreg" 

	version("0.1.1", md5="91f0ab1ca69c1e65e74f3da3b9bac7ae")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-misc3d", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-mbend", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
