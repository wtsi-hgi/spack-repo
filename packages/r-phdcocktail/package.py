# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhdcocktail(RPackage):
	"""Enhance the Ease of R Experience as an Emerging Researcher

	A toolkit of functions to help: i) effortlessly transform collected data into a 
  publication ready format, ii) generate insightful visualizations from clinical data, iii) report
  summary statistics in a publication-ready format, iv) efficiently export, save and reload R objects
  within the framework of R projects.
	"""
	
	homepage = "https://dahhamalsoud.github.io/phdcocktail/"
	cran = "phdcocktail" 

	version("0.1.0", md5="e43382b0d72b3d04177bc96ea4941f61")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-here", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
