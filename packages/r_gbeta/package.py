# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGbeta(RPackage):
	"""Generalized Beta and Beta Prime Distributions

	Density, distribution function, quantile function, and random generation for the generalized Beta and Beta prime distributions. The family of generalized Beta distributions is conjugate for the Bayesian binomial model, and the generalized Beta prime distribution is the posterior distribution of the relative risk in the Bayesian 'two Poisson samples' model when a Gamma prior is assigned to the Poisson rate of the reference group and a Beta prime prior is assigned to the relative risk. References: Laurent (2012) <doi:10.1214/11-BJPS139>, Hamza & Vallois (2016) <doi:10.1016/j.spl.2016.03.014>, Chen & Novick (1984) <doi:10.3102/10769986009002163>.
	"""
	
	homepage = "https://github.com/stla/gbeta"
	cran = "gbeta" 

	version("0.1.0", md5="1e302dc09fd4c3230e80c3b6ca8fa9ca")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-gsl", type=("build", "run"))
	depends_on("r-runuran", type=("build", "run"))
	depends_on("r-rcppnumerical", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
