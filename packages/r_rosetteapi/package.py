# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRosetteapi(RPackage):
	"""'Rosette' API

	'Rosette' is an API for multilingual text analysis and information
    extraction. More information can be found at <https://developer.rosette.com>.
	"""
	
	homepage = "https://developer.rosette.com"
	cran = "rosetteApi" 

	version("1.14.4", md5="e7b72f045b7905913d002a562e660eef")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
