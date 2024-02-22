# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMnda(RPackage):
	"""Multiplex Network Differential Analysis (MNDA)

	Interactions between different biological entities are crucial for the function of biological systems. 
    In such networks, nodes represent biological elements, such as genes, proteins and microbes, and their interactions can be defined by edges, which can be either binary or weighted.
    The dysregulation of these networks can be associated with different clinical conditions such as diseases and response to treatments. 
    However, such variations often occur locally and do not concern the whole network. 
    To capture local variations of such networks, we propose multiplex network differential analysis (MNDA). 
    MNDA allows to quantify the variations in the local neighborhood of each node (e.g. gene) between the two given clinical states, and to test for statistical significance of such variation.
    Yousefi et al. (2023) <doi:10.1101/2023.01.22.525058>.
	"""
	
	cran = "mnda" 

	version("1.0.9", md5="97c5e6359bb640ac84881b4ea8e4d1f9")

	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-keras", type=("build", "run"))
	depends_on("r-tensorflow", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-aggregation", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
