# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBedassle(RPackage):
	"""Quantifies Effects of Geo/Eco Distance on Genetic
Differentiation

	Provides functions that allow users to quantify the relative 
	contributions of geographic and ecological distances to empirical patterns of genetic 
	differentiation on a landscape.  Specifically, we use a custom Markov chain 
	Monte Carlo (MCMC) algorithm, which is used to estimate the parameters of the 
	inference model, as well as functions for performing MCMC diagnosis and assessing 
	model adequacy.
	"""
	
	cran = "BEDASSLE" 

	version("1.6.1", md5="542260c8bb0602de2a5b6bff555da16c")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-emdbook", type=("build", "run"))
