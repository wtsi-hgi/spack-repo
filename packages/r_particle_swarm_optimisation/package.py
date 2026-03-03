# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParticleSwarmOptimisation(RPackage):
	"""Optimisation with Particle Swarm Optimisation

	A toolbox to create a particle swarm optimisation (PSO), the package contains two classes: the Particle and the Particle Swarm, this two class is used to run the PSO with methods to easily print, plot and save the result.
	"""
	
	cran = "particle.swarm.optimisation" 

	version("1.0", md5="391aa2d193566f08a601f49bf43c7bf0")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
