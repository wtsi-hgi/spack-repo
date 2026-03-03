# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStan4bart(RPackage):
	"""Bayesian Additive Regression Trees with Stan-Sampled Parametric
Extensions

	Fits semiparametric linear and multilevel models with non-parametric additive Bayesian additive regression tree (BART; Chipman, George, and McCulloch (2010) <doi:10.1214/09-AOAS285>) components and Stan (Stan Development Team (2021) <https://mc-stan.org/>) sampled parametric ones. Multilevel models can be expressed using 'lme4' syntax (Bates, Maechler, Bolker, and Walker (2015) <doi:10.18637/jss.v067.i01>).
	"""
	
	homepage = "https://github.com/vdorie/stan4bart"
	cran = "stan4bart" 

	version("0.0-7", md5="d7646fb364f24fc8eb34af1013cb92d1")

	depends_on("r@3.5.0:", type=("build", "run"))
	depends_on("r-dbarts@0.9.20:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcppparallel@5.1.1:", type=("build", "run"))
	depends_on("r-bh@1.72.0.3:", type=("build", "run"))
	depends_on("r-rcpp@1.0.5:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.7:", type=("build", "run"))
