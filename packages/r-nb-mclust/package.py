# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNbMclust(RPackage):
	"""Negative Binomial Model-Based Clustering

	Model-based clustering of high-dimensional non-negative
             data that follow Generalized Negative Binomial distribution. All functions 
             in this package applies to either continuous or integer data. Correlation
            between variables are allowed, while samples are assumed to be independent.
	"""
	
	cran = "NB.MClust" 

	version("1.1.1", md5="3d8ffcbbedea2ba575508175d1b9addd")

	depends_on("r@3.3.3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
