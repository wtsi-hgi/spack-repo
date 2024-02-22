# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQueryup(RPackage):
	"""Query the 'UniProtKB' REST API

	Retrieve protein information from
    the 'UniProtKB' REST API (see <https://www.uniprot.org/help/api_queries>).
	"""
	
	homepage = "https://github.com/VoisinneG/queryup"
	cran = "queryup" 

	version("1.0.5", md5="dfca4d5165accae1aafa67c13ee6675f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
