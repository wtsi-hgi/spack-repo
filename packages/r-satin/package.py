# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSatin(RPackage):
	"""Visualisation and Analysis of Ocean Data Derived from Satellites

	With 'satin' functions, visualisation, data extraction and further analysis like producing climatologies from several images, and anomalies of satellite derived ocean data can be easily done.  Reading functions can import a user defined geographical extent of data stored in netCDF files.  Currently supported ocean data sources include NASA's Oceancolor web page <https://oceancolor.gsfc.nasa.gov/>, sensors VIIRS-SNPP; MODIS-Terra; MODIS-Aqua; and SeaWiFS.  Available variables from this source includes chlorophyll concentration, sea surface temperature (SST), and several others.  Data sources specific for SST that can be imported too includes Pathfinder AVHRR <https://www.ncei.noaa.gov/products/avhrr-pathfinder-sst> and GHRSST <https://www.ghrsst.org/>.  In addition, ocean productivity data produced by Oregon State University <http://sites.science.oregonstate.edu/ocean.productivity/> can also be handled previous conversion from HDF4 to HDF5 format.  Many other ocean variables can be processed by importing netCDF data files from two European Union's Copernicus Marine Service databases <https://marine.copernicus.eu/>, namely Global Ocean Physical Reanalysis and Global Ocean Biogeochemistry Hindcast.
	"""
	
	homepage = "https://github.com/hvillalo/satin"
	cran = "satin" 

	version("1.1.0", md5="33964e84cd5ba22377f99c6b47e82440")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-pbsmapping", type=("build", "run"))
	depends_on("r-splancs", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
