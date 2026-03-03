# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAgriwater(RPackage):
	"""Evapotranspiration and Energy Fluxes Spatial Analysis

	Spatial modeling of energy balance and actual 
    evapotranspiration using satellite images and meteorological data. 
    Options of satellite are: Landsat-8 (with and without thermal bands), 
    Sentinel-2 and MODIS. Respectively spatial resolutions are 30, 100, 
    10 and 250 meters. User can use data from a single meteorological 
    station or a grid of meteorological stations (using any spatial 
    interpolation method). Silva, Teixeira, and Manzione (2019) <doi:10.1016/j.envsoft.2019.104497>.
	"""
	
	cran = "agriwater" 

	version("1.0.2", md5="5c6b5adefea7e5c475740c1d33f340fd")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
