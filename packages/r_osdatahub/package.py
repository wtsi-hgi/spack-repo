# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROsdatahub(RPackage):
	"""Easier Interaction with the Ordnance Survey Data Hub

	Ordnance Survey ('OS') is the national mapping agency for Great 
    Britain and produces a large variety of mapping and geospatial products. 
    Much of OS's data is available via the OS Data Hub <https://osdatahub.os.uk/>, 
    a platform that hosts both free and premium data products. 'osdatahub' 
    provides a user-friendly way to access, query, and download these data.
	"""
	
	cran = "osdatahub" 

	version("0.2.0", md5="86eee50740417c1bb31ff2a7f40f4b85")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-geojsonsf", type=("build", "run"))
	depends_on("r-geos", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
