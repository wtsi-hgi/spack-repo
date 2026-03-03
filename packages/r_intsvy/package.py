# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntsvy(RPackage):
	"""International Assessment Data Manager

	
  Provides tools for importing, merging, and analysing data from 
  international assessment studies (TIMSS, PIRLS, PISA, ICILS, and PIAAC).
	"""
	
	homepage = "https://daniel-caro.com/r-intsvy/"
	cran = "intsvy" 

	version("2.9", md5="c09807a4f59b112e06196856277e6e78")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-memisc", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
