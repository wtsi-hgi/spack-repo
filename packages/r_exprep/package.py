# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExprep(RPackage):
	"""Experiment Repetitions

	Allows to calculate the probabilities  of occurrences of an event in a 
 great number of repetitions of Bernoulli experiment, through the application of  
 the local and the integral theorem of De Moivre Laplace, and the theorem of Poisson. 
 Gives the possibility to show the results graphically and analytically, and to compare
 the results obtained by the application of the above  theorems with those calculated by
 the direct application of the Binomial formula. Is basically useful for educational
 purposes. 
	"""
	
	cran = "ExpRep" 

	version("1.0", md5="abe7f44ff8c6dfd308ce0f50f25108ae")

