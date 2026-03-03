# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRwsearch(RPackage):
	"""Lazy Search in R Packages, Task Views, CRAN, the Web. All-in-One
Download

	Search by keywords in R packages, task views, CRAN, the web and display the results in the console or in txt, html or pdf files. Download the package documentation (html index, README, NEWS, pdf manual, vignettes, source code, binaries) with a single instruction. Visualize the package dependencies and CRAN checks. Compare the package versions, unload and install the packages and their dependencies in a safe order. Explore CRAN archives. Use the above functions for task view maintenance. Access web search engines from the console thanks to 80+ bookmarks. All functions accept standard and non-standard evaluation.
	"""
	
	cran = "RWsearch" 

	version("5.1.4", md5="8d16a7fb6649c55e6ff43eb603ad45b5")
	version("5.0.5", md5="ea8ee3157119a855f997d0e0eb8e3eef")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-brew", type=("build", "run"))
	depends_on("r-latexpdf", type=("build", "run"))
	depends_on("r-networkd3", type=("build", "run"))
	depends_on("r-sig", type=("build", "run"))
	depends_on("r-sos", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
