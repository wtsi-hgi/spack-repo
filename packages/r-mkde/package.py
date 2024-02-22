# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMkde(RPackage):
	"""2D and 3D Movement-Based Kernel Density Estimates (MKDEs)

	Provides functions to compute and visualize movement-based kernel density estimates (MKDEs) for animal utilization distributions in 2 or 3 spatial dimensions.
	"""
	
	cran = "mkde" 

	version("0.2", md5="9e5e9cf2fac2558c5a7e2a06b45af4b7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
