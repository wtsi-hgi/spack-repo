# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRestatapi(RPackage):
	"""Search and Retrieve Data from Eurostat Database

	Eurostat is the statistical office of the European Union and provides high quality statistics for Europe.
             Large set of the data is disseminated through the Eurostat database (<https://ec.europa.eu/eurostat/web/main/data/database>). 
             The tools are using the REST API with the Statistical Data and Metadata eXchange (SDMX) Web Services 
             (<https://wikis.ec.europa.eu/pages/viewpage.action?pageId=44165555>) to search and download data from 
             the Eurostat database using the SDMX standard. 
	"""
	
	homepage = "https://github.com/eurostat/restatapi"
	cran = "restatapi" 

	version("0.23.1", md5="48cb9ccb4dadbf8acc4dcafffd7330dd")
	version("0.22.5", md5="a89bbe9326056be3e5fd99b5b70752e9")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
