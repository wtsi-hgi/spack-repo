# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRerddapxtracto(RPackage):
	"""Extracts Environmental Data from 'ERDDAP' Web Services

	Contains three functions that access
    environmental data from any 'ERDDAP' data web service. The rxtracto() function extracts
    data along a trajectory for a given "radius" around the point. The
    rxtracto_3D() function extracts data in a box. The rxtractogon() function
    extracts data in a polygon. All of those three function use the 'rerddap' package
    to extract the data, and should work with any 'ERDDAP' server.
    There are also two functions, plotBBox() and plotTrack() that use the 'plotdap'
    package to simplify the creation of maps of the data.
	"""
	
	homepage = "https://github.com/rmendels/rerddapXtracto"
	cran = "rerddapXtracto" 

	version("1.2.0", md5="8e2ab2a5ef0d3cbd17f7edd15d2070d8")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-parsedate", type=("build", "run"))
	depends_on("r-plotdap@0.0.5:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rerddap@0.8:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
