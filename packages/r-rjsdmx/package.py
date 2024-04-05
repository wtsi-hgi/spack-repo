# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRjsdmx(RPackage):
	"""R Interface to SDMX Web Services

	Provides functions to retrieve data and metadata from providers 
			 that disseminate data by means of SDMX web services. 
			 SDMX (Statistical Data and Metadata eXchange) is a standard that 
			 has been developed with the aim of simplifying the exchange of 
			 statistical information. 
			 More about the SDMX standard and the SDMX Web Services 
			 can be found at: <https://sdmx.org>.
	"""
	
	homepage = "https://github.com/amattioc/SDMX/"
	cran = "RJSDMX" 

	version("3.1-0", md5="f7717972d6259357cc8536f81b928e5e")
	version("3.0-6", md5="63ce196ebfd74e25ccdfe28c2f7dad9a")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rjava@0.8.8:", type=("build", "run"))
	depends_on("r-zoo@1.6.4:", type=("build", "run"))
	depends_on("openjdk@8:", type=("build", "link", "run"))
