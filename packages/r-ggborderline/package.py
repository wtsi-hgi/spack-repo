# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgborderline(RPackage):
	"""Line Plots that Pop

	A set of geometries to make line plots a little bit nicer. Use 
    along with 'ggplot2' to:
    - Improve the clarity of line plots with many overlapping lines
    - Draw more realistic worms.
	"""
	
	homepage = "https://github.com/wurli/ggborderline"
	cran = "ggborderline" 

	version("0.2.0", md5="060048f76a16f505825851bb22b64f59")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
