# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClusvis(RPackage):
	"""Gaussian-Based Visualization of Gaussian and Non-Gaussian
Model-Based Clustering

	Gaussian-Based Visualization of Gaussian and Non-Gaussian Model-Based Clustering done on any type of data. Visualization is based on the probabilities of classification.
	"""
	
	cran = "ClusVis" 

	version("1.2.0", md5="8d405843b3cb57f073f6c20bb0ce066d")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rmixmod", type=("build", "run"))
	depends_on("r-varsellcm@2.1:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
