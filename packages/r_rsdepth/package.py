# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsdepth(RPackage):
	"""Ray Shooting Depth (i.e. RS Depth) Functions for Bivariate
Analysis

	Ray Shooting Depth functions are provided for bivariate analysis. This mainly includes functions for computing the bivariate depth as well as RS median. Drawing functions for depth bags are also provided. 
	"""
	
	cran = "rsdepth" 

	version("0.1-22", md5="7e3395a9e7e7206d18f08ca12f52da59")

	depends_on("r@2.4:", type=("build", "run"))
