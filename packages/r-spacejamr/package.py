# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpacejamr(RPackage):
	"""Simulate Spatial Bernoulli Networks

	Social network analysis is becoming commonplace in many social 
    science disciplines, but access to useful network data, especially 
    among marginalized populations, still remains a formidable challenge. 
    This package mitigates that problem by providing tools to simulate spatial 
    Bernoulli networks as proposed in Carter T. Butts 
    (2002, ISBN:978-0-493-72676-2), "Spatial models of large-scale interpersonal            
    networks." Using this package, network analysts can simulate a spatial point 
    process or sequence with a given number of nodes inside a geographical 
    boundary and estimate the probability of a tie formation between all node 
    pairs. When simulating a network, an analyst can choose between five spatial
    interaction functions. The package also enables quick comparison of summary             
    statistics for simulated networks and provides simple to use plotting 
    methods for its classes that return plots which can be further refined with 
    the 'ggplot2' package.
	"""
	
	homepage = "https://github.com/dscolby/spacejamr"
	cran = "spacejamr" 

	version("0.2.1", md5="295900121cc8edb532671f227c4055ad")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-crsuggest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-spatstat-random", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
