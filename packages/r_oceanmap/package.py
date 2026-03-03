# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROceanmap(RPackage):
	"""A Plotting Toolbox for 2D Oceanographic Data

	Plotting toolbox for 2D oceanographic data (satellite data, sea surface temperature, chlorophyll, ocean fronts & bathymetry). Recognized classes and formats include netcdf, Raster, '.nc' and '.gz' files.
	"""
	
	cran = "oceanmap" 

	version("0.1.6", md5="efc066e1e751caa07d59b68465c3c7d4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-mapdata", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-extrafont", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggedit", type=("build", "run"))
	depends_on("r-sf@0.9.7:", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("imagemagick", type=("build", "link", "run"))
