# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGcpbayes(RPackage):
	"""Bayesian Meta-Analysis of Pleiotropic Effects Using Group
Structure

	Run a Gibbs sampler for a multivariate Bayesian sparse group selection model with Dirac, continuous and hierarchical spike prior for detecting pleiotropy on the traits. This package is designed for summary statistics containing estimated regression coefficients and its estimated covariance matrix. The methodology is available from: Baghfalaki, T., Sugier, P. E., Truong, T., Pettitt, A. N., Mengersen, K., & Liquet, B. (2021) <doi:10.1002/sim.8855>.
	"""
	
	homepage = "https://github.com/tbaghfalaki/GCPBayes"
	cran = "GCPBayes" 

	version("4.2.0", md5="7c5a7a152f4b532d2a6718a0fac6cbc0")
	version("4.1.0", md5="63eb90bee6fe0c7a41164ee8cb827d2b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-invgamma", type=("build", "run"))
	depends_on("r-gdata", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-postpack", type=("build", "run"))
	depends_on("r-wiqid", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
