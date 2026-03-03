# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrackdem(RPackage):
	"""Particle Tracking and Demography

	Obtain population density and body size structure, using video material or image sequences as input. Functions assist in the creation of image sequences from videos, background detection and subtraction, particle identification and tracking. An artificial neural network can be trained for noise filtering. The goal is to supply accurate estimates of population size, structure and/or individual behavior, for use in  evolutionary and ecological studies.
	"""
	
	homepage = "https://github.com/marjoleinbruijning/trackdem"
	cran = "trackdem" 

	version("0.6", md5="2c74ad2b647566a94667acfaed831731")

	depends_on("r-png", type=("build", "run"))
	depends_on("r-neuralnet", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("python@2.7:", type=("build", "link", "run"))
	depends_on("ffmpeg", type=("build", "link", "run"))
