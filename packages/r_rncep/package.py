# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRncep(RPackage):
	"""Obtain, Organize, and Visualize NCEP Weather Data

	Contains functions to retrieve, organize, and visualize weather data from the NCEP/NCAR Reanalysis (<http://www.esrl.noaa.gov/psd/data/gridded/data.ncep.reanalysis.html>) and NCEP/DOE Reanalysis II (<http://www.esrl.noaa.gov/psd/data/gridded/data.ncep.reanalysis2.html>) datasets.  Data are queried via the Internet and may be obtained for a specified spatial and temporal extent or interpolated to a point in space and time.  We also provide functions to visualize these weather data on a map.  There are also functions to simulate flight trajectories according to specified behavior using either NCEP wind data or data specified by the user.
	"""
	
	homepage = "https://www.esrl.noaa.gov/psd/data/gridded/reanalysis/"
	cran = "RNCEP" 

	version("1.0.10", md5="8da1c7156e2ecfbd42658703655f894e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-tgp", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
