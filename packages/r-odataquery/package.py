# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROdataquery(RPackage):
	"""Querying on 'OData'

	Make querying on 'OData' easier. It exposes an 'ODataQuery' object
    that can be manipulated and provides features such as selection, filtering
    and ordering.
	"""
	
	cran = "ODataQuery" 

	version("0.5.3", md5="896b47efd8be2e248bbf031d906e3e41")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
