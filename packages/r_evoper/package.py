# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvoper(RPackage):
	"""Evolutionary Parameter Estimation for 'Repast Simphony' Models

	The EvoPER, Evolutionary Parameter Estimation for Individual-based Models is an extensible 
      package providing optimization driven parameter estimation methods using metaheuristics  and 
      evolutionary computation techniques (Particle Swarm Optimization, Simulated Annealing, Ant Colony Optimization 
      for continuous domains, Tabu Search, Evolutionary Strategies, ...)  which could be more efficient and require, 
      in some cases, fewer model evaluations than alternatives relying on experimental design.  Currently there 
      are built in support for models developed with 'Repast Simphony'  Agent-Based framework (<https://repast.github.io/>)  
      and with NetLogo (<https://ccl.northwestern.edu/netlogo/>) which are the most used frameworks for Agent-based modeling. 
	"""
	
	homepage = "https://github.com/antonio-pgarcia/evoper"
	cran = "evoper" 

	version("0.5.0", md5="607a27e09e797624043de6a105da94ab")

	depends_on("r-rrepast", type=("build", "run"))
	depends_on("r-futile-logger", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rnetlogo", type=("build", "run"))
