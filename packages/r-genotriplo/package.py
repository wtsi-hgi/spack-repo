# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenotriplo(RPackage):
	"""Genotyping Triploids (or Diploids) from Luminescence Data

	Genotyping of triploid individuals from luminescence data (marker probeset A and B). Works also for diploids.
	Two main functions: Run_Clustering() that regroups individuals with a same genotype based on proximity and
	Run_Genotyping() that assigns a genotype to each cluster. For Shiny interface use: launch_GenoShiny().
	"""
	
	cran = "GenoTriplo" 

	version("1.0.3", md5="6029ba0d77e4287f11a1a608e7933edc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rmixmod", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
