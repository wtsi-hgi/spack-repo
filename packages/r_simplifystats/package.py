# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimplifystats(RPackage):
	"""Simplifies Pairwise Statistical Analyses

	Pairwise group comparisons are often performed. While there are many packages that can perform these analyses, often it is the case that only a subset of comparisons are desired. 'SimplifyStats' performs pairwise comparisons and returns the results in a tidy fashion.
	"""
	
	cran = "SimplifyStats" 

	version("2.0.4", md5="42d3cb06f7b3cd31151f6861030639c3")

	depends_on("r-assertthat@0.2:", type=("build", "run"))
	depends_on("r-tibble@1.4.2:", type=("build", "run"))
	depends_on("r-dplyr@0.7.4:", type=("build", "run"))
	depends_on("r-broom@0.4.4:", type=("build", "run"))
	depends_on("r-moments@0.14:", type=("build", "run"))
