# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDocreview(RPackage):
	"""Opinionated Documentation Checking

	High quality documentation can make for a great experience for your users. You can use 'docreview' to check that your R package documentation passes a number of configurable checks relating to documentation content.
	"""
	
	homepage = "https://thisisnic.github.io/docreview/"
	cran = "docreview" 

	version("0.0.1", md5="1060bb8f7d799d958b441347509e5159")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-parsermd", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-quanteda", type=("build", "run"))
	depends_on("r-quanteda-textstats", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
