# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RN2h4(RPackage):
	"""Handling Methods for Naver News Text Crawling

	Provides some functions to get Korean text sample from news articles in
             Naver which is popular news portal service <https://news.naver.com/> in Korea.
	"""
	
	homepage = "https://forkonlp.github.io/N2H4/"
	cran = "N2H4" 

	version("0.8.4", md5="1f716c3fd7782640df4dd511366ba29f", url="https://cran.r-project.org/src/contrib/N2H4_0.8.4.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
