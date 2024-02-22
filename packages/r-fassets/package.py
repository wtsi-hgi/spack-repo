# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFassets(RPackage):
	"""Rmetrics - Analysing and Modelling Financial Assets

	A collection of functions to manage, to investigate and to analyze data sets of financial 
  assets from different points of view.
	"""
	
	homepage = "https://r-forge.r-project.org/projects/rmetrics/"
	cran = "fAssets" 

	version("4023.85", md5="35c3071f5a6be8575c5d7bcf29a80c61")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-timedate", type=("build", "run"))
	depends_on("r-timeseries", type=("build", "run"))
	depends_on("r-fbasics", type=("build", "run"))
	depends_on("r-fmultivar", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-sn", type=("build", "run"))
	depends_on("r-ecodist", type=("build", "run"))
	depends_on("r-mvnormtest", type=("build", "run"))
	depends_on("r-energy", type=("build", "run"))
