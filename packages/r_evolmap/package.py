# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvolmap(RPackage):
	"""Dynamic and Interactive Maps

	Dynamic and Interactive Maps with R, powered by 'leaflet' <https://leafletjs.com>. 'evolMap' generates a web page with interactive and dynamic maps to which you can add geometric entities (points, lines or colored geographic areas), and/or markers with optional links between them. The dynamic ability of these maps allows their components to evolve over a continuous period of time or by periods.
	"""
	
	cran = "evolMap" 

	version("1.2.33", md5="2ee4c0da2d11a34b9bae411739ee4bd1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
