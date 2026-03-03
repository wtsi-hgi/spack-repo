# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultilevelpsa(RPackage):
	"""Multilevel Propensity Score Analysis

	Conducts and visualizes propensity score analysis for multilevel, 
  or clustered data. Bryer & Pruzek (2011) <doi:10.1080/00273171.2011.636693>.
	"""
	
	homepage = "http://github.com/jbryer/multilevelPSA"
	cran = "multilevelPSA" 

	version("1.2.5", md5="9f5f9de928b66822cf2c6ed888940a0f")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r@3:", type=("build", "run"))
	depends_on("r-psagraphics", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-party", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
