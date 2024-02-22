# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThredds(RPackage):
	"""Crawler for Navigating THREDDS Catalogs

	Provides a crawler for programmatically navigating THREDDS Data Server (<https://www.unidata.ucar.edu/software/tds/>) 
  catalogs, and access dataset metadata and resources.
	"""
	
	homepage = "https://github.com/BigelowLab/thredds"
	cran = "thredds" 

	version("0.1-4", md5="69ebd958310ff87dca90636e0c347f01")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
