# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWikilake(RPackage):
	"""Scrape Lake Metadata Tables from Wikipedia

	Scrape lake metadata tables from Wikipedia <https://www.wikipedia.org/>. 
	"""
	
	homepage = "https://github.com/jsta/wikilake"
	cran = "wikilake" 

	version("0.7.0", md5="3302d0823d23ad9ac59d2491f63bc1da")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-wikipedir", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-selectr", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
