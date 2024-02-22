# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROnpoint(RPackage):
	"""Helper Functions for Point Pattern Analysis

	
  Growing collection of helper functions for point pattern analysis. Most functions
  are designed to work with the 'spatstat' (<http://spatstat.org>) package. The focus of 
  most functions are either null models or summary functions for spatial point patterns. 
  For a detailed description of all null models and summary functions, see 
  Wiegand and Moloney (2014, ISBN:9781420082548).
	"""
	
	homepage = "https://r-spatialecology.github.io/onpoint/"
	cran = "onpoint" 

	version("1.0.5", md5="548b468679b6d82c35e9b13f23398f5a")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-random", type=("build", "run"))
