# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBnptsclust(RPackage):
	"""A Bayesian Nonparametric Algorithm for Time Series Clustering

	Performs the algorithm for time series clustering described in Nieto-Barajas and Contreras-Cristan (2014).
	"""
	
	cran = "BNPTSclust" 

	version("2.0", md5="07a00a24ead47d5e14b6a1094088cf71")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
