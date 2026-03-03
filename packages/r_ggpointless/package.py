# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgpointless(RPackage):
	"""Additional Geometries and Stats for 'ggplot2'

	An (aspirational) collection of additional geometries and 
    statistics for 'ggplot2'. 
	"""
	
	homepage = "https://flrd.github.io/ggpointless/"
	cran = "ggpointless" 

	version("0.1.0", md5="cdac964efb92300231c6b5e949dcbd6b")

	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
