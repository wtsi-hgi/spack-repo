# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultivariance(RPackage):
	"""Measuring Multivariate Dependence Using Distance Multivariance

	Distance multivariance is a measure of dependence which can be used to detect 
    and quantify dependence of arbitrarily many random vectors. The necessary functions are
    implemented in this packages and examples are given. It includes: distance multivariance, 
    distance multicorrelation, dependence structure detection, tests of independence and
    copula versions of distance multivariance based on the Monte Carlo empirical transform.
    Detailed references are given in the package description, as starting point for the 
    theoretic background we refer to:
    B. Böttcher, Dependence and Dependence Structures: Estimation and Visualization Using 
    the Unifying Concept of Distance Multivariance. Open Statistics, Vol. 1, No. 1 (2020), 
    <doi:10.1515/stat-2020-0001>.
	"""
	
	cran = "multivariance" 

	version("2.4.1", md5="20f7deb84e0b247b5db123ba3239f3f5")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-microbenchmark", type=("build", "run"))
