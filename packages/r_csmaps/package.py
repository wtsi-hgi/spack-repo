# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCsmaps(RPackage):
	"""Preformatted Maps of Norway that Don't Need Geolibraries

	Provides datasets containing preformatted maps of Norway at
    the county, municipality, and ward (Oslo only) level for redistricting in 
    2024, 2020, 2018, and 2017. Multiple layouts are provided (normal, split, 
    and with an insert for Oslo), allowing the user to rapidly create choropleth
    maps of Norway without any geolibraries.
	"""
	
	homepage = "https://www.csids.no/csmaps/"
	cran = "csmaps" 

	version("2023.5.22", md5="7377018219bb012cc3975046cb658a71")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
