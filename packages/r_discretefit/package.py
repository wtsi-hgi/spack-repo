# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiscretefit(RPackage):
	"""Simulated Goodness-of-Fit Tests for Discrete Distributions

	Implements fast Monte Carlo simulations for 
    goodness-of-fit (GOF) tests for discrete distributions. This 
    includes tests based on the Chi-squared statistic, the 
    log-likelihood-ratio (G^2) statistic, the Freeman-Tukey 
    (Hellinger-distance) statistic, the Kolmogorov-Smirnov 
    statistic, the Cramer-von Mises statistic as described in 
    Choulakian, Lockhart and Stephens (1994) <doi:10.2307/3315828>, 
    and the root-mean-square statistic, see Perkins, 
    Tygert, and Ward (2011) <doi:10.1016/j.amc.2011.03.124>.
	"""
	
	homepage = "https://github.com/josh-mc/discretefit"
	cran = "discretefit" 

	version("0.1.2", md5="ae524694c347adfd79245a85ee2d922b")

	depends_on("r-rcpp", type=("build", "run"))
