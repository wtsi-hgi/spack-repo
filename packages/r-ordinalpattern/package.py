# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrdinalpattern(RPackage):
	"""Tests Based on Ordinal Patterns

	Ordinal patterns describe the dynamics of a time series by looking at the ranks of subsequent observations. By comparing ordinal patterns of two times series, Schnurr (2014) <doi:10.1007/s00362-013-0536-8> defines a robust and non-parametric dependence measure: the ordinal pattern coefficient. Functions to calculate this and a method to detect a change in the pattern coefficient proposed in Schnurr and Dehling (2017) <doi:10.1080/01621459.2016.1164706> are provided.
	"""
	
	cran = "ordinalpattern" 

	version("0.2.3", md5="7b5433e81fe8d3ed0b14772e7561faba")

	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
