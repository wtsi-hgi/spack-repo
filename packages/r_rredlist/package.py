# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRredlist(RPackage):
	"""'IUCN' Red List Client

	'IUCN' Red List (<http://apiv3.iucnredlist.org/api/v3/docs>) client.
    The 'IUCN' Red List is a global list of threatened and endangered species.
    Functions cover all of the Red List 'API' routes. An 'API' key is required.
	"""
	
	homepage = "https://github.com/ropensci/rredlist"
	cran = "rredlist" 

	version("0.7.1", md5="00ad7972b9e08e060ff7d8b76d17024f")

	depends_on("r-crul@0.3.8:", type=("build", "run"))
	depends_on("r-jsonlite@1.1:", type=("build", "run"))
