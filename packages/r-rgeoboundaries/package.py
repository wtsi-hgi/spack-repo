# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgeoboundaries(RPackage):
	"""geoBoundaries Client

	Provides access to the geoBoundaries international boundary database <https://www.geoboundaries.org>, a NSF and foundation supported dataset 
 of subnational boundaries around the globe.  Methods allow you to access data directly from the API <https://www.geoboundaries.org/api/current/> to 
 query for the geometric boundaries for any country, globally. For more details, refer to the publication by Runfola et al. (2020) <doi:10.1371/journal.pone.0231866>.
	"""
	
	homepage = "https://github.com/wmgeolab/rgeoboundaries"
	cran = "rgeoboundaries" 

	version("1.3", md5="2f3c846d03f951c8f54ba93318d322cc")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-crul@1.4:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-sf@1:", type=("build", "run"))
	depends_on("r-hoardr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-countrycode@1.2:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
