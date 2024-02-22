# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRwc(RPackage):
	"""Random Walk Covariance Models

	Code to facilitate simulation and inference when connectivity is defined by underlying random walks. Methods for spatially-correlated pairwise distance data are especially considered. This provides core code to conduct analyses similar to that in Hanks and Hooten (2013) <doi:10.1080/01621459.2012.724647>.
	"""
	
	cran = "rwc" 

	version("1.11", md5="9547ea1bb4c5c138d8b732f934f1b377")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
