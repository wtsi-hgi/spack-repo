# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRepec(RPackage):
	"""Access RePEc Data Through API

	Utilities for accessing RePEc (Research Papers in Economics)
    through a RESTful API. You can request a code and get detailed
    information at the following page: <https://ideas.repec.org/api.html>.
	"""
	
	homepage = "https://github.com/chrMongeau/repec"
	cran = "repec" 

	version("0.1.0", md5="d2b0f6f726d4121491d3ce81f69e9c28")

	depends_on("r-jsonlite", type=("build", "run"))
