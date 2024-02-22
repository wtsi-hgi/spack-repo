# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrecipe(RPackage):
	"""Precipitation R Recipes

	An open-access tool/framework to download, validate, visualize, and
  analyze multi-source precipitation data. More information and an example of implementation can
  be found in Vargas Godoy and Markonis (2023,
  <doi:10.1016/j.envsoft.2023.105711>).
	"""
	
	homepage = "https://github.com/MiRoVaGo/pRecipe"
	cran = "pRecipe" 

	version("3.0.1-3", md5="d9f718650882c3d5b0880613a4e47159")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-openair", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("proj@6:", type=("build", "link", "run"))
	depends_on("gdal@3:", type=("build", "link", "run"))
	depends_on("netcdf-c@4:", type=("build", "link", "run"))
