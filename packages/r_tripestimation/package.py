# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTripestimation(RPackage):
	"""Metropolis Sampler and Supporting Functions for Estimating
Animal Movement from Archival Tags and Satellite Fixes

	Data handling and estimation functions for animal movement
    estimation from archival or satellite tags. Helper functions are included
    for making image summaries binned by time interval from Markov Chain Monte Carlo
    simulations. 
	"""
	
	homepage = "https://github.com/Trackage/tripEstimation"
	cran = "tripEstimation" 

	version("0.0-46", md5="e9320e22b376f450fa96c013fa40e7db")

	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-reproj", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
