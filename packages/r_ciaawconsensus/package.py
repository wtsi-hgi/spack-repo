# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCiaawconsensus(RPackage):
	"""Isotope Ratio Meta-Analysis

	Calculation of consensus values for atomic weights, isotope amount ratios, and isotopic abundances with the associated uncertainties using multivariate meta-regression approach for consensus building.
	"""
	
	cran = "CIAAWconsensus" 

	version("1.3", md5="bb77248d8b74dce7db3f6e7f7941b24c")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
