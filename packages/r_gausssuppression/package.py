# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGausssuppression(RPackage):
	"""Tabular Data Suppression using Gaussian Elimination

	A statistical disclosure control tool to protect tables by suppression 
    using the Gaussian elimination secondary suppression algorithm. A suggestion is 
    to start by working with functions SuppressSmallCounts() and 
    SuppressDominantCells(). These functions use primary suppression functions for 
    the minimum frequency rule and the dominance rule, respectively. Novel 
    functionality for suppression of disclosive cells is also included. General 
    primary suppression functions can be supplied as input to the general working 
    horse function, GaussSuppressionFromData(). Suppressed frequencies can be 
    replaced by synthetic decimal numbers as described in 
    Langsrud (2019) <doi:10.1007/s11222-018-9848-9>.
	"""
	
	homepage = "https://github.com/statisticsnorway/GaussSuppression"
	cran = "GaussSuppression" 

	version("0.8.3", md5="ce1a6db09607e319a2b70ffd59268a96")
	version("0.8.0", md5="7db021c754fd07d21d18a675c35127d8")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ssbtools@1.5:", type=("build", "run"))
	depends_on("r-regsdc@0.7:", type=("build", "run"))
