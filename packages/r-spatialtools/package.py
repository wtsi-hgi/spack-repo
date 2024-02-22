# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialtools(RPackage):
	"""Tools for Spatial Data Analysis

	Tools for spatial data analysis.  Emphasis on kriging.  Provides functions for prediction and simulation.  Intended to be relatively straightforward, fast, and flexible.
	"""
	
	cran = "SpatialTools" 

	version("1.0.5", md5="51c6fb69b87220aa97694512bc505c86")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-spbayes@0.3:", type=("build", "run"))
	depends_on("r-rcpp@0.9.10:", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.3:", type=("build", "run"))
