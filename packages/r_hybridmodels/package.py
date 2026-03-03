# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHybridmodels(RPackage):
	"""An R Package for the Stochastic Simulation of Disease Spreading
in Dynamic Networks

	Simulates stochastic hybrid models for transmission of infectious
    diseases in dynamic networks. It is a metapopulation model in which each
    node in the network is a sub-population and disease spreads within nodes
    and among them, combining two approaches: stochastic simulation algorithm
    (<doi:10.1146/annurev.physchem.58.032806.104637>) and individual-based
    approach, respectively. Equations that models spread within nodes are
    customizable and there are two link types among nodes: migration and
    influence (commuting). More information in Fernando S. Marques,
    Jose H. H. Grisi-Filho, Marcos Amaku et al. (2020) <doi:10.18637/jss.v094.i06>.
	"""
	
	homepage = "https://github.com/fernandosm/hybridModels"
	cran = "hybridModels" 

	version("0.3.7", md5="edcefee4431c8cb43c3f51c8226a820e")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gillespiessa", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
