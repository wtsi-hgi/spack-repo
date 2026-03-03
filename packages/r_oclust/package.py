# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROclust(RPackage):
	"""Gaussian Model-Based Clustering with Outliers

	Provides a function to detect and trim outliers in Gaussian mixture model-based clustering using methods described in Clark and McNicholas (2022) <arXiv:1907.01136>.
	"""
	
	cran = "oclust" 

	version("0.2.0", md5="72b44d369be15b358f5ac9b84a8c9bb5")

	depends_on("r-entropy", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-mixture", type=("build", "run"))
	depends_on("r-dbscan", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
