# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpiderbar(RPackage):
	"""Parse and Test Robots Exclusion Protocol Files and Rules

	The 'Robots Exclusion Protocol' <https://www.robotstxt.org/orig.html> documents
    a set of standards for allowing or excluding robot/spider crawling of different areas of
    site content. Tools are provided which wrap The 'rep-cpp' <https://github.com/seomoz/rep-cpp>
    C++ library for processing these 'robots.txt' files.
	"""
	
	homepage = "https://github.com/hrbrmstr/spiderbar"
	cran = "spiderbar" 

	version("0.2.5", md5="9a5a078c070b43e93a273396354a3c3a")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
