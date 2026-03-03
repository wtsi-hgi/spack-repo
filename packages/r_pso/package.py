# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPso(RPackage):
	"""Particle Swarm Optimization

	Provides an implementation of particle swarm optimisation consistent with the standard PSO 2007/2011 by Maurice Clerc. Additionally a number of ancillary routines are provided for easy testing and graphics.
	"""
	
	cran = "pso" 

	version("1.0.4", md5="6c4345d275001abe1c3154b7afa36610")

	depends_on("r@2.10:", type=("build", "run"))
