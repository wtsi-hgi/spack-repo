# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArulesviz(RPackage):
	"""Visualizing Association Rules and Frequent Itemsets

	Extends package 'arules' with various visualization techniques for association rules and itemsets. The package also includes several interactive visualizations for rule exploration. Michael Hahsler (2017) <doi:10.32614/RJ-2017-047>.
	"""
	
	homepage = "https://github.com/mhahsler/arulesViz"
	cran = "arulesViz" 

	version("1.5-2", md5="979f688945f7f164a46a383ff82e8be7")

	depends_on("r-arules@1.6:", type=("build", "run"))
	depends_on("r-seriation", type=("build", "run"))
	depends_on("r-vcd", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
