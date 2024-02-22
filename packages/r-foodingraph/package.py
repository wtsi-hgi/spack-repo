# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFoodingraph(RPackage):
	"""Food Network Inference and Visualization

	Displays a weighted undirected food graph from an adjacency matrix.
    Can perform confidence-interval bootstrap inference with mutual information
    or maximal information coefficient.
    Based on my Master 1 internship at the Bordeaux Population Health center.
    References : Reshef et al. (2011) <doi:10.1126/science.1205438>,
    Meyer et al. (2008) <doi:10.1186/1471-2105-9-461>,
    Liu et al. (2016) <doi:10.1371/journal.pone.0158247>.
	"""
	
	homepage = "https://github.com/vgasque/foodingraph/"
	cran = "foodingraph" 

	version("0.1.0", md5="58a6d1f557f470e53033603e92529e52")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-minerva", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-labeling", type=("build", "run"))
