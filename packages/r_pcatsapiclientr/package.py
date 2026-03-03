# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcatsapiclientr(RPackage):
	"""'PCATS' API Client

	Provides an R interface to the 'PCATS' API
    <https://pcats.research.cchmc.org/api/__docs__/>,
    allowing R users to submit tasks and retrieve results.
	"""
	
	cran = "pcatsAPIclientR" 

	version("1.1.0", md5="332ee6ad72d52c8096301931cb8859f9")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
