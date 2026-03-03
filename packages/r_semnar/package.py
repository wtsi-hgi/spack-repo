# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemnar(RPackage):
	"""Constructing and Interacting with Databases of Presentations

	Provides methods for constructing and maintaining a database of presentations in R. The presentations are either ones that the user gives or gave or presentations at a particular event or event series. The package also provides a plot method for the interactive mapping of the presentations using 'leaflet' by grouping them according to country, city, year and other presentation attributes. The markers on the map come with popups providing presentation details (title, institution, event, links to materials and events, and so on).
	"""
	
	cran = "semnar" 

	version("0.8.1", md5="2b07235c93c1b76fafc17d4af2fe4cb1")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-parsedate", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-urlshortener", type=("build", "run"))
