# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidygeorss(RPackage):
	"""Tidy GeoRSS

	
    In order to easily integrate geoRSS data into analysis,
    'tidygeoRSS' parses 'geo' feeds and returns 
    tidy simple features data frames.
	"""
	
	homepage = "https://github.com/RobertMyles/tidygeoRSS"
	cran = "tidygeoRSS" 

	version("0.0.1", md5="f991fa0a5722d06ad277ea9c6df90c22")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-xml2@1.3.1:", type=("build", "run"))
	depends_on("r-httr@1.4.1:", type=("build", "run"))
	depends_on("r-anytime@0.3.7:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-tidyrss@2.0.2:", type=("build", "run"))
	depends_on("r-jsonlite@1.6.1:", type=("build", "run"))
	depends_on("r-strex@1.2:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr@0.3.3:", type=("build", "run"))
	depends_on("r-sf@0.9.1:", type=("build", "run"))
	depends_on("r-rlang@0.4.6:", type=("build", "run"))
