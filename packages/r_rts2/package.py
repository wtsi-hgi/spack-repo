# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRts2(RPackage):
	"""Real-Time Disease Surveillance

	Supports modelling real-time case data to facilitate the real-time
    surveillance of infectious diseases and other point phenomena. The package provides automated computational grid generation over
    an area of interest with methods to map covariates between geographies, model fitting including spatially aggregated case counts, 
    and predictions and visualisation. Both Bayesian and maximum likelihood methods are provided. Log-Gaussian Cox Processes are described by 
    Diggle et al. (2013) <doi:10.1214/13-STS441> and we provide both the low-rank approximation for Gaussian processes 
    described by Solin and Särkkä (2020) <doi:10.1007/s11222-019-09886-w> and Riutort-Mayol et al (2020) <arXiv:2004.11408> and the
    nearest neighbour Gaussian process described by Datta et al (2016) <doi:10.1080/01621459.2015.1044091>. 'cmdstanr' can be downloaded at <https://mc-stan.org/cmdstanr/>.
	"""
	
	cran = "rts2" 

	version("0.7.2", md5="74dd4bed0f43d1d22cc7d5b30296234b", url="https://cran.r-project.org/src/contrib/rts2_0.7.2.tar.gz")
	version("0.6.1", md5="b8fe632120bebe2aa2b867bb71522f13", url="https://cran.r-project.org/src/contrib/rts2_0.6.1.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sf@1.0.14:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools@2.1.1:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.32:", type=("build", "run"))
	depends_on("r-glmmrbase@0.7.1:", type=("build", "run"))
	depends_on("r-sparsechol@0.2.2:", type=("build", "run"))
