# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWildmeta(RPackage):
	"""Cluster Wild Bootstrapping for Meta-Analysis

	Conducts single coefficient tests and multiple-contrast hypothesis tests of meta-regression models using cluster wild bootstrapping, based on methods examined in Joshi, Pustejovsky, and Beretvas (2022) <DOI:10.1002/jrsm.1554>. 
	"""
	
	homepage = "https://meghapsimatrix.github.io/wildmeta/index.html"
	cran = "wildmeta" 

	version("0.3.2", md5="0406d32b18efc40f374bec6172443f41")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-clubsandwich@0.5.4:", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-robumeta", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
