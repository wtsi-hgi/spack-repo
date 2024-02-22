# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGoodfibes(RPackage):
	"""Detection and Reconstruction of Muscle Fibers from diceCT Image
Data

	Reconstruction of muscle fibers from image stacks using textural analysis. Includes functions for tracking, smoothing, cleaning, plotting and exporting muscle fibers. Also calculates basic fiber properties (e.g., length and curvature).
	"""
	
	cran = "GoodFibes" 

	version("0.1.10", md5="b5bce8f00740dc84e898bbb72048968a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-imager", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-concaveman", type=("build", "run"))
	depends_on("r-prodlim", type=("build", "run"))
	depends_on("r-splines2", type=("build", "run"))
