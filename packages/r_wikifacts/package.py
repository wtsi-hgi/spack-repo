# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWikifacts(RPackage):
	"""Get Facts and Data from Wikipedia and Wikidata

	Query Wikidata and get facts from current and historic Wikipedia main pages.  
	"""
	
	cran = "wikifacts" 

	version("0.4.2", md5="600ed82e16468833e991f4c6c930b86f")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
