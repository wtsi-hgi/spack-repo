# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdiutils(RPackage):
	"""An API Client for the Environmental Data Initiative Repository

	A client for the Environmental Data Initiative repository REST API. The 'EDI' data repository <https://portal.edirepository.org/nis/home.jsp> is for publication and reuse of ecological data with emphasis on metadata accuracy and completeness. It is built upon the 'PASTA+' software stack <https://pastaplus-core.readthedocs.io/en/latest/index.html#> and was developed in collaboration with the US 'LTER' Network <https://lternet.edu/>. 'EDIutils' includes functions to search and access existing data, evaluate and upload new data, and assist other data management tasks common to repository users.
	"""
	
	homepage = "https://github.com/ropensci/EDIutils"
	cran = "EDIutils" 

	version("1.0.3", md5="cd48b215d80f95f1498a232cbd6956a1")

	depends_on("r-curl", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
