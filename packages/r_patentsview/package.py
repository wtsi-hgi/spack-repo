# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPatentsview(RPackage):
	"""An R Client to the 'PatentsView' API

	Provides functions to simplify the 'PatentsView' API
    (<https://patentsview.org/apis/purpose>) query language,
    send GET and POST requests to the API's seven endpoints, and parse the data
    that comes back.
	"""
	
	homepage = "https://docs.ropensci.org/patentsview/index.html"
	cran = "patentsview" 

	version("0.3.0", md5="f43121db7a8998faac632413d4249906")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
