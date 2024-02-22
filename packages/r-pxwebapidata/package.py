# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPxwebapidata(RPackage):
	"""PX-Web Data by API

	Function to read PX-Web data into R via API. The example code reads data from the three national statistical institutes, Statistics Norway, Statistics Sweden and Statistics Finland.
	"""
	
	homepage = "https://github.com/statisticsnorway/PxWebApiData"
	cran = "PxWebApiData" 

	version("0.9.0", md5="39ca0e9b7b1ad9dd2c97964a09db30a8")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rjstat", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-pxweb", type=("build", "run"))
