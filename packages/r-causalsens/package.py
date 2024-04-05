# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCausalsens(RPackage):
	"""Selection Bias Approach to Sensitivity Analysis for Causal
Effects

	The causalsens package provides functions to perform sensitivity analyses and to study how various assumptions about selection bias affects estimates of causal effects.
	"""
	
	homepage = "https://www.mattblackwell.org/software/causalsens/"
	cran = "causalsens" 

	version("0.1.3", md5="db43054ff9f07af833e297a4b2da5222")
	version("0.1.2", md5="508c4226c159ebb43814c6a1d4662b1d")

	depends_on("r@3:", type=("build", "run"))
