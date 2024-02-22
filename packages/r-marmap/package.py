# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMarmap(RPackage):
	"""Import, Plot and Analyze Bathymetric and Topographic Data

	Import xyz data from the NOAA (National Oceanic and Atmospheric Administration, <https://www.noaa.gov>), GEBCO (General Bathymetric Chart of the Oceans, <https://www.gebco.net>) and other sources, plot xyz data to prepare publication-ready figures, analyze xyz data to extract transects, get depth / altitude based on geographical coordinates, or calculate z-constrained least-cost paths.
	"""
	
	homepage = "https://github.com/ericpante/marmap"
	cran = "marmap" 

	version("1.0.10", md5="9a73bca528d625ab2f6f7b44818b2180")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-gdistance", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-shape", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-adehabitatma", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
