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

	version("1.0.0", md5="45b1c4ce02eea7bc3bf9e5a18bc0fe99")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate@2:", type=("build", "run"))
	depends_on("r-data-table@1.12.8:", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-memoise@1.1:", type=("build", "run"))
	depends_on("r-rcppsimdjson@0.1.1:", type=("build", "run"))
