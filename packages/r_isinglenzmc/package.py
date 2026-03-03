# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsinglenzmc(RPackage):
	"""Monte Carlo for Classical Ising Model

	Classical Ising Model is a land mark system in statistical physics.The model explains the physics of spin glasses and magnetic materials, and cooperative phenomenon in general, for example phase transitions and neural networks.This package provides utilities to simulate one dimensional Ising Model with Metropolis and Glauber Monte Carlo with single flip dynamics in periodic boundary conditions. Utility functions for exact solutions are provided.
	"""
	
	cran = "isingLenzMC" 

	version("0.2.5", md5="2c186416c38f8cb9e0f8390c795340a1")

	depends_on("r@3:", type=("build", "run"))
