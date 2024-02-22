# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultisom(RPackage):
	"""Clustering a Data Set using Multi-SOM Algorithm

	Implements two versions of the algorithm namely: stochastic and batch. The package determines also the best number of clusters and offers to the user the best clustering scheme from different results.
	"""
	
	homepage = "https://sites.google.com/site/malikacharrad/research/multisom-package"
	cran = "multisom" 

	version("1.3", md5="cd7f8bb7712c22e12b3ccf22af9b408b")

	depends_on("r@3.1.3:", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-kohonen", type=("build", "run"))
