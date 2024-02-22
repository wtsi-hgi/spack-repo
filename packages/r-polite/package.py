# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolite(RPackage):
	"""Be Nice on the Web

	Be responsible when scraping data from websites by following polite principles: introduce yourself, ask for permission, take slowly and never ask twice. 
	"""
	
	homepage = "https://github.com/dmi3kno/polite"
	cran = "polite" 

	version("0.1.3", md5="7cce19672daaf2fca5d20d1f5c483198")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-ratelimitr", type=("build", "run"))
	depends_on("r-robotstxt", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
