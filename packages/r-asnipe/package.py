# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsnipe(RPackage):
	"""Animal Social Network Inference and Permutations for Ecologists

	Implements several tools that are used in animal social network analysis, as described in Whitehead (2007) Analyzing Animal Societies <University of Chicago Press> and Farine & Whitehead (2015) <doi: 10.1111/1365-2656.12418>. In particular, this package provides the tools to infer groups and generate networks from observation data, perform permutation tests on the data, calculate lagged association rates, and performed multiple regression analysis on social network data.
	"""
	
	cran = "asnipe" 

	version("1.1.17", md5="8f357d33a0c0f4360bba2e0d3a22269e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
