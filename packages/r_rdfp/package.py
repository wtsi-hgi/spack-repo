# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdfp(RPackage):
	"""An Implementation of the 'DoubleClick for Publishers' API

	Functions to interact with the 'Google DoubleClick for Publishers (DFP)' API 
    <https://developers.google.com/ad-manager/api/start> (recently renamed to 
    'Google Ad Manager'). This package is automatically compiled from the API WSDL 
    (Web Service Description Language) files to dictate how the API is structured. 
    Theoretically, all API actions are possible using this package; however, care 
    must be taken to format the inputs correctly and parse the outputs correctly. 
    Please see the 'Google Ad Manager' API reference <https://developers.google.com/ad-manager/api/rel_notes> 
    and this package's website <https://stevenmmortimer.github.io/rdfp/> for more 
    information, documentation, and examples.
	"""
	
	homepage = "https://github.com/StevenMMortimer/rdfp"
	cran = "rdfp" 

	version("0.1.4", md5="939d1ca1fb1f559c2629a71c0dc4e142")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr@1.4:", type=("build", "run"))
	depends_on("r-curl@3.3:", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
	depends_on("r-xml@3.98.1.19:", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-xml2@1.2:", type=("build", "run"))
	depends_on("r-readr@1.3.1:", type=("build", "run"))
	depends_on("r-data-table@1.12:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
