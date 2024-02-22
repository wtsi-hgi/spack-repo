# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnomads(RPackage):
	"""An R Interface to the NOAA Operational Model Archive and
Distribution System

	An interface to the National Oceanic and Atmospheric Administration's Operational Model Archive and Distribution System (NOMADS, see <https://nomads.ncep.noaa.gov/> for more information) that allows R users to quickly and efficiently download global and regional weather model data for processing.  rNOMADS currently supports a variety of models ranging from global weather data to an altitude of over 40 km, to high resolution regional weather models, to wave and sea ice models.  rNOMADS can retrieve binary data in grib format as well as import ascii data directly into R by interfacing with the GrADS-DODS system.
	"""
	
	homepage = "<https://r-forge.r-project.org/projects/rnomads/"
	cran = "rNOMADS" 

	version("2.5.3", md5="6cb5c12629a58e345ba8813523210fd4")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rvest@0.3.2:", type=("build", "run"))
	depends_on("r-stringr@1.2:", type=("build", "run"))
	depends_on("r-fields@9:", type=("build", "run"))
	depends_on("r-geomap@2.3.5:", type=("build", "run"))
	depends_on("r-mba", type=("build", "run"))
	depends_on("r-httr@1.4.4:", type=("build", "run"))
	depends_on("r-xml@3.99.0.3:", type=("build", "run"))
	depends_on("r-uuid@0.1.2:", type=("build", "run"))
