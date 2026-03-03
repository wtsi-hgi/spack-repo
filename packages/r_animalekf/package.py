# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnimalekf(RPackage):
	"""Extended Kalman Filters for Animal Movement

	Synthetic generation of 1-D and 2-D correlated random walks (CRWs) for animal movement with behavioral switching, and particle filter estimation of movement parameters from observed trajectories using Extended Kalman Filter (EKF) model. See Ackerman (2018) <https://digital.library.temple.edu/digital/collection/p245801coll10/id/499150>.
	"""
	
	cran = "animalEKF" 

	version("1.2", md5="72854c15897b018d0a1e6e26324f6ac8")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-deldir", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-bezier", type=("build", "run"))
	depends_on("r-hdinterval", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
