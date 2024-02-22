# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvapore(RPackage):
	"""Evapotranspiration R Recipes

	An R-based application for exploratory data analysis of global EvapoTranspiration (ET) datasets. 
  'evapoRe' enables users to download, validate, visualize, and analyze multi-source ET data across various spatio-temporal scales.
  Also, the package offers calculation methods for estimating potential ET (PET), including temperature-based approaches described in : Oudin et al., (2005) <doi:10.1016/j.jhydrol.2004.08.026>.
  'evapoRe' supports hydrological modeling, climate studies, agricultural research, and other data-driven fields by facilitating access to ET data and offering powerful analysis capabilities.
  Users can seamlessly integrate the package into their research applications and explore diverse ET data at different resolutions.
	"""
	
	homepage = "https://github.com/AkbarR1184/evapoRe"
	cran = "evapoRe" 

	version("1.0.0", md5="b4480c3c56f358953543d691a0358046")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-precipe", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("proj@6:", type=("build", "link", "run"))
	depends_on("gdal@3:", type=("build", "link", "run"))
	depends_on("netcdf-c@4:", type=("build", "link", "run"))
