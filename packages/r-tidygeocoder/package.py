# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidygeocoder(RPackage):
	"""Geocoding Made Easy

	An intuitive interface for getting data from geocoding services. 
	"""
	
	homepage = "https://jessecambon.github.io/tidygeocoder/"
	cran = "tidygeocoder" 

	version("1.0.5", md5="299f5610401944a4d3dce57a60a0b83a")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
