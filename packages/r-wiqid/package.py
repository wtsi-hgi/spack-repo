# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWiqid(RPackage):
	"""Quick and Dirty Estimates for Wildlife Populations

	Provides simple, fast functions for maximum likelihood and Bayesian estimates of wildlife population parameters, suitable for use with simulated data or bootstraps. Early versions were indeed quick and dirty, but optional error-checking routines and meaningful error messages have been added. Includes single and multi-season occupancy, closed capture population estimation, survival, species richness and distance measures.
	"""
	
	homepage = "https://mmeredith.net/R/wiqid/"
	cran = "wiqid" 

	version("0.3.3", md5="53fd78b2367d6c11850968069433f6b5")

	depends_on("r-hdinterval", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mcmcoutput", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
