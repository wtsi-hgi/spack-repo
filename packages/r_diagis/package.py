# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiagis(RPackage):
	"""Diagnostic Plot and Multivariate Summary Statistics of Weighted
Samples from Importance Sampling

	Fast functions for effective sample size, weighted multivariate 
    mean, variance, and quantile computation, and weight diagnostic plot for 
    generic importance sampling type or other probability weighted samples.
	"""
	
	homepage = "https://github.com/helske/diagis/"
	cran = "diagis" 

	version("0.2.3", md5="40c3c69f0daebc87ee7deb76b7af115d")

	depends_on("r-coda", type=("build", "run"))
	depends_on("r-ggplot2@2.1:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
