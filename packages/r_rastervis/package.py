# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRastervis(RPackage):
	"""Visualization Methods for Raster Data

	Methods for enhanced visualization and interaction with raster data. It implements visualization methods for quantitative data and categorical data, both for univariate and multivariate rasters. It also provides methods to display spatiotemporal rasters, and vector fields. See the website for examples.
	"""
	
	homepage = "https://oscarperpinan.github.io/rastervis/"
	cran = "rasterVis" 

	version("0.51.6", md5="9e0a042f2e7058b73b32e8207fdbfd74")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-lattice@0.22.5:", type=("build", "run"))
	depends_on("r-raster@3.4.13:", type=("build", "run"))
	depends_on("r-terra@1.7.17:", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-hexbin", type=("build", "run"))
	depends_on("r-sp@1.0.6:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
