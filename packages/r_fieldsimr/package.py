# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFieldsimr(RPackage):
	"""Simulation of Plot Errors and Phenotypes in Plant Breeding Field
Trials

	Simulates plot data in field trials for multiple 
	traits across multiple environments. Its core function generates plot errors comprising 1) 
	a spatially correlated error term, 2) a random error term, and 3) an extraneous error 
	term. Spatially correlated errors are simulated using either bivariate interpolation 
	or a two-dimensional autoregressive process of order one (AR1:AR1). The three error 
	terms are combined at a user-defined ratio. Plot phenotypes can be generated 
	by combining the simulated errors with genetic values (e.g. true, simulated 
	or predicted). 'FieldSimR' provides wrapper functions to simulate genetic values for 
	multiple traits across multiple environments using the 'R' package 'AlphaSimR'.
	"""
	
	homepage = "https://github.com/crWerner/fieldsimr"
	cran = "FieldSimR" 

	version("1.2.0", md5="e75813f6790c05cfa74a1eef859a4c23")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-interp", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-mbend", type=("build", "run"))
