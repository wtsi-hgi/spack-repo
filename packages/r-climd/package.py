# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClimd(RPackage):
	"""Generating Rainfall Rasters from IMD NetCDF Data

	The developed function is a comprehensive tool for the analysis of India Meteorological Department (IMD) NetCDF rainfall data. Specifically designed to process high-resolution daily
             gridded rainfall datasets. It provides four key functions to process IMD NetCDF rainfall data and create rasters for various temporal scales, including annual, seasonal, monthly, and weekly
             rainfall. For method details see, Malik, A. (2019).<DOI:10.1007/s12517-019-4454-5>. It supports different aggregation methods, such as sum, min, max, mean, and standard deviation. These functions
             are designed for spatio-temporal analysis of rainfall patterns, trend analysis,geostatistical modeling of rainfall variability, identifying rainfall anomalies and extreme events and can be an input
             for hydrological and agricultural models.
	"""
	
	cran = "CLimd" 

	version("0.1.0", md5="5eebcb0a48e41d2ee6b11bdda08786af")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-qpdf", type=("build", "run"))
