# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCdcplaces(RPackage):
	"""Access the 'CDC PLACES' API

	Allows users to seamlessly query several 'CDC PLACES' APIs (<https://data.cdc.gov/browse?q=PLACES%20&sortBy=relevance>)
    by geography, state, measure, and release year. This package also contains a
    function to explore the available measures for each release year. 
	"""
	
	homepage = "https://github.com/brendensm/CDCPLACES"
	cran = "CDCPLACES" 

	version("1.1.5", md5="bcce052ec1a13c0ee6b18ae7821df5eb")
	version("1.1.4", md5="24d6a7b2bc89ffaa077a2794508bc148")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tigris", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-usa", type=("build", "run"))
