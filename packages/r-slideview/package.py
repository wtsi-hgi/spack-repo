# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlideview(RPackage):
	"""Compare Raster Images Side by Side with a Slider

	Create a side-by-side view of raster(image)s with an interactive 
    slider to switch between regions of the images. This can be especially useful
    for image comparison of the same region at different time stamps.
	"""
	
	homepage = "https://r-spatial.github.io/slideview/"
	cran = "slideview" 

	version("0.2.0", md5="84a0dc6f58d341b54eb23bd6ff61f586")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
