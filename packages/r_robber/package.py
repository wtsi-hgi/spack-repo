# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobber(RPackage):
	"""Using Block Model to Estimate the Robustness of Ecological
Network

	Implementation of a variety of methods to compute
    the robustness of ecological interaction networks with binary interactions 
    as described in <doi:10.1002/env.2709>. In particular, using the Stochastic 
    Block Model and its bipartite counterpart, the Latent Block Model to put a 
    parametric model on the network, allows the comparison of the robustness of 
    networks differing in species richness and number of interactions. It also
    deals with networks that are partially sampled and/or with missing values. 
	"""
	
	homepage = "https://github.com/Chabert-Liddell/robber"
	cran = "robber" 

	version("0.2.4", md5="258ca041572670ac5dcf3718dd7fd057")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-blockmodels@1.1.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gremlins", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-pammtools", type=("build", "run"))
	depends_on("r-partitions", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
