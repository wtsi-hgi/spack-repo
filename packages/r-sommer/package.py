# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSommer(RPackage):
	"""Solving Mixed Model Equations in R

	Structural multivariate-univariate linear mixed model solver for estimation of multiple random effects with unknown variance-covariance structures (e.g., heterogeneous and unstructured) and known covariance among levels of random effects (e.g., pedigree and genomic relationship matrices) (Covarrubias-Pazaran, 2016 <doi:10.1371/journal.pone.0156744>; Maier et al., 2015 <doi:10.1016/j.ajhg.2014.12.006>; Jensen et al., 1997). REML estimates can be obtained using the Direct-Inversion Newton-Raphson and Direct-Inversion Average Information algorithms for the problems r x r (r being the number of records) or using the Henderson-based average information algorithm for the problem c x c (c being the number of coefficients to estimate). Spatial models can also be fitted using the two-dimensional spline functionality available.
	"""
	
	cran = "sommer" 

	version("4.3.4", md5="26bc955d439be6b0a4db6a8faf44e6bc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix@1.1.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
