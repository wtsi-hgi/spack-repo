# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimfinapi(RPackage):
	"""Accessing 'SimFin' Data

	Through simfinapi, you can intuitively access the 'SimFin'
    Web-API (<https://www.simfin.com/>) to make 'SimFin' data easily
    available in R. To obtain an 'SimFin' API key (and thus to use this
    package), you need to register at <https://app.simfin.com/login>.
	"""
	
	homepage = "https://github.com/matthiasgomolka/simfinapi"
	cran = "simfinapi" 

	version("0.2.4", md5="c8dce2b941b3f3ed4ea81c8d264f7038")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
	depends_on("r-checkmate@2:", type=("build", "run"))
	depends_on("r-data-table@1.12.8:", type=("build", "run"))
	depends_on("r-future-apply@1.4:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-memoise@1.1:", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-rcppsimdjson@0.1.1:", type=("build", "run"))
