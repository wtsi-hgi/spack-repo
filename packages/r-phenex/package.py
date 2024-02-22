# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhenex(RPackage):
	"""Auxiliary Functions for Phenological Data Analysis

	Provides some easy-to-use functions for 
	spatial analyses of (plant-) phenological data 
	sets and satellite observations of vegetation.
	"""
	
	cran = "phenex" 

	version("1.4-5", md5="56ec593309f94e6d67331771f402245d")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-deoptim", type=("build", "run"))
