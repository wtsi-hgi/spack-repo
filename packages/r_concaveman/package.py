# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConcaveman(RPackage):
	"""A Very Fast 2D Concave Hull Algorithm

	The concaveman function ports the 'concaveman' (<https://github.com/mapbox/concaveman>) library from 'mapbox'. It computes the concave polygon(s) for one or several set of points.
	"""
	
	homepage = "https://joelgombin.github.io/concaveman/"
	cran = "concaveman" 

	version("1.1.0", md5="3b5693cb7c0ab371dc7605129a5ad2be")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-v8", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("gdal@2.0.0:", type=("build", "link", "run"))
	depends_on("geos@3.3.0:", type=("build", "link", "run"))
	depends_on("proj@4.8.0:", type=("build", "link", "run"))
