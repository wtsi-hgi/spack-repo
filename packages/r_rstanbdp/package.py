# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRstanbdp(RPackage):
	"""Bayesian Deming Regression for Method Comparison

	Regression methods to quantify the relation 
    between two measurement methods are provided by this package. The
    focus is on a Bayesian Deming regressions family. With a Bayesian
    method the Deming regression can be run in a traditional fashion or
    can be run in a robust way just decreasing the degree of freedom
    d.f. of the sampling distribution. With d.f. = 1 an extremely robust
    Cauchy distribution can be sampled. Moreover, models for dealing
    with heteroscedastic data are also provided. For reference see
    G. Pioda (2024) <https://piodag.github.io/bd1/>.
	"""
	
	cran = "rstanbdp" 

	version("0.0.2", md5="9bd2f09fe5e5f71801dfbf1c83b4f0ac")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-rstantools@2.4:", type=("build", "run"))
	depends_on("r-rrcov", type=("build", "run"))
	depends_on("r-mixtools", type=("build", "run"))
	depends_on("r-bayestestr", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
