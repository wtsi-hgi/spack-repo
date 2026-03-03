# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROhsome(RPackage):
	"""An 'ohsome API' Client

	A client that grants access to the power of the 'ohsome API'
    from R. It lets you analyze the rich data source of the 
    'OpenStreetMap (OSM)' history. You can retrieve the geometry of 'OSM' 
    data at specific points in time, and you can get aggregated statistics 
    on the evolution of 'OSM' elements and specify your own temporal, 
    spatial and/or thematic filters.
	"""
	
	homepage = "https://github.com/GIScience/ohsome-r"
	cran = "ohsome" 

	version("0.2.2", md5="af0841a0dd6f863b121d7457f62bd5a2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-geojsonsf", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
