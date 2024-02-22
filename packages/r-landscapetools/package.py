# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLandscapetools(RPackage):
	"""Landscape Utility Toolbox

	Provides utility functions for some of the less-glamorous tasks involved
    in landscape analysis. It includes functions to coerce raster data to the
    common tibble format and vice versa, it helps with flexible reclassification
    tasks of raster data and it provides a function to merge multiple raster.
    Furthermore, 'landscapetools' helps landscape scientists to visualize their
    data by providing optional themes and utility functions to plot single
    landscapes, rasterstacks, -bricks and lists of raster.
	"""
	
	homepage = "https://ropensci.github.io/landscapetools/"
	cran = "landscapetools" 

	version("0.5.0", md5="9a8c3325d061b07c4392b92e915cef3b")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
