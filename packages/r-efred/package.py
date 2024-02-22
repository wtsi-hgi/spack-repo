# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REfred(RPackage):
	"""Fetch Data from the Federal Reserve Economic Database

	
      Interact with the FRED API, <https://fred.stlouisfed.org/docs/api/fred/>, 
      to fetch observations across economic series;
      find information about different economic sources, releases, series, etc.;
      conduct searches by series name, attributes, or tags; and determine the 
      latest updates. Includes functions for creating panels of related variables 
      with minimal effort and datasets containing data sources, releases, and 
      popular FRED tags.
	"""
	
	cran = "eFRED" 

	version("0.1.0", md5="5dd5a86bee06f8874185b5084d79ed4c")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
