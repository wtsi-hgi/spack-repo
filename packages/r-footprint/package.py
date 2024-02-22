# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFootprint(RPackage):
	"""Calculate Air Travel Emissions

	A handy tool to calculate carbon footprints from
    air travel based on three-letter International Air Transport Association (IATA) airport codes or latitude and longitude.
    footprint first calculates the great-circle distance between departure and arrival 
    destinations. It then uses the Department of Environment, Food & Rural Affairs (DEFRA) 
    greenhouse gas conversion factors for business air travel to estimate the carbon footprint.
    These conversion factors consider trip length, flight class (e.g. economy, business), and emissions 
    metric (e.g. carbon dioxide equivalent, methane).
	"""
	
	homepage = "https://github.com/acircleda/footprint"
	cran = "footprint" 

	version("0.1", md5="c948b389bdb4d18d2b2dbc2ed80549df")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-airportr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
