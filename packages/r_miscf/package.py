# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMiscf(RPackage):
	"""Miscellaneous Functions

	Various functions for random number generation, density 
             estimation, classification, curve fitting, and spatial 
             data analysis.
	"""
	
	cran = "miscF" 

	version("0.1-5", md5="65ab168bc23ce2b133ec7796b4464234")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-mass@7.3.45:", type=("build", "run"))
	depends_on("r-r2jags@0.5.7:", type=("build", "run"))
	depends_on("r-mcmcpack@1.2.4:", type=("build", "run"))
	depends_on("r-mvtnorm@0.9.9992:", type=("build", "run"))
