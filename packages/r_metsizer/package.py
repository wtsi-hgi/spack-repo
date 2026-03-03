# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetsizer(RPackage):
	"""A Shiny App for Sample Size Estimation in Metabolomic
Experiments

	Provides a Shiny application to estimate the sample size required 
    for a metabolomic experiment to achieve a desired statistical power. 
    Estimation is possible with or without available data from a pilot study. 
	"""
	
	cran = "MetSizeR" 

	version("2.0.0", md5="779776d4c0ade2304e1b4a4827bbe316")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-metabolanalyze", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-vroom", type=("build", "run"))
