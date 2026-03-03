# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHybridmicrobiomes(RPackage):
	"""Analysis of Host-Associated Microbiomes from Hybrid Organisms

	A set of tools to analyze and visualize the relationships between host-associated microbiomes of hybrid organisms and those of their progenitor species. Though not necessary, installing the microViz package is recommended as a check for phyloseq objects. To install microViz from R Universe use the following command: install.packages("microViz", repos = c(davidbarnett = "https://david-barnett.r-universe.dev", getOption("repos"))). To install microViz from GitHub use the following commands: install.packages("devtools") followed by devtools::install_github("david-barnett/microViz").
	"""
	
	cran = "HybridMicrobiomes" 

	version("0.1.1", md5="e9b7079c4be561cce83c5e2c8f9d3511")

	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-compositions", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-permanova", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-stereomorph", type=("build", "run"))
	depends_on("r-phyloseq", type=("build", "run"))
