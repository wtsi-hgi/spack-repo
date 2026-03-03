# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnassqs(RPackage):
	"""Access Data from the NASS 'Quick Stats' API

	Interface to access data via the United States Department of 
  Agriculture's National Agricultural Statistical Service (NASS) 'Quick Stats' 
  web API <https://quickstats.nass.usda.gov/api>. Convenience functions 
  facilitate building queries based on available parameters and valid parameter 
  values. This product uses the NASS API but is not endorsed or certified by NASS.
	"""
	
	homepage = "https://docs.ropensci.org/rnassqs/"
	cran = "rnassqs" 

	version("0.6.1", md5="2d08aed6f8190e29d91efafc028aa8f1")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
