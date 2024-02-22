# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTracker(RPackage):
	"""Infrastructure for Running, Cycling and Swimming Data from
GPS-Enabled Tracking Devices

	Provides infrastructure for handling running, cycling and swimming data from GPS-enabled tracking devices within R. The package provides methods to extract, clean and organise workout and competition data into session-based and unit-aware data objects of class 'trackeRdata' (S3 class). The information can then be visualised, summarised, and analysed through flexible and extensible methods. Frick and Kosmidis (2017) <doi: 10.18637/jss.v082.i07>, which is updated and maintained as one of the vignettes, provides detailed descriptions of the package and its methods, and real-data demonstrations of the package functionality.
	"""
	
	homepage = "https://github.com/trackerproject/trackeR"
	cran = "trackeR" 

	version("1.6.0", md5="fe55a4e10485d497733c92e566043b29")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-scam", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-ggmap", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
