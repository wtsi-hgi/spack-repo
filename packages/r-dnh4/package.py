# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDnh4(RPackage):
	"""Crawling for Daum News Text

	Provides some utils to get Korean text sample from news articles
            in Daum which is popular news portal service in Korea.
	"""
	
	homepage = "https://forkonlp.github.io/DNH4/"
	cran = "DNH4" 

	version("0.1.12", md5="a3b204f5b4fd4dad3e31b13f9e478fa1", url="https://cran.r-project.org/src/contrib/DNH4_0.1.12.tar.gz")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
