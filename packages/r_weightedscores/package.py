# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWeightedscores(RPackage):
	"""Weighted Scores Method for Regression Models with Dependent Data

	The weighted scores method and composite likelihood information criteria as an intermediate step for variable/correlation selection for longitudinal ordinal and count data in Nikoloulopoulos, Joe and Chaganty (2011)  <doi:10.1093/biostatistics/kxr005>, Nikoloulopoulos (2016) <doi:10.1002/sim.6871> and Nikoloulopoulos (2017) <arXiv:1510.07376>.
	"""
	
	cran = "weightedScores" 

	version("0.9.5.3", md5="cb7acefb6935b391a50fbb42d76bec38")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
