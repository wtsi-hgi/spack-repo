# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGcite(RPackage):
	"""Google Citation Parser

	Scrapes Google Citation pages and creates data frames of 
    citations over time.
	"""
	
	cran = "gcite" 

	version("0.10.1", md5="2a46ffcc341b2ad65270e05f5bd577cd")

	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-wordcloud", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
