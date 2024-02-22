# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSgmodel(RPackage):
	"""Solves a Generic Stochastic Growth Model with a Representative
Agent

	It computes the solutions to a generic stochastic growth model for a given set of user supplied parameters. It includes
    the solutions to the model, plots of the solution, 	
    a summary of the features of the model, a function that covers different types of consumption preferences,
    and a function that computes the moments of a Markov process.	
	Merton, Robert C (1971) <doi:10.1016/0022-0531(71)90038-X>,
	Tauchen, George (1986) <doi:10.1016/0165-1765(86)90168-0>,
	Wickham, Hadley (2009, ISBN:978-0-387-98140-6 ).
	"""
	
	cran = "sgmodel" 

	version("0.1.2", md5="eee552f6659a39b0420624238ac448f6")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ramify", type=("build", "run"))
	depends_on("r-rtauchen", type=("build", "run"))
