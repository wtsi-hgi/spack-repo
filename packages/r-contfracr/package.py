# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RContfracr(RPackage):
	"""Continued Fraction Generators and Evaluators

	Converts numbers to continued fractions and back again. A solver for Pell's Equation is provided.  The method for calculating roots in continued fraction form is provided without published attribution in such places as Professor Emeritus Jonathan Lubin, <http://www.math.brown.edu/jlubin/> and his post to StackOverflow, <https://math.stackexchange.com/questions/2215918> , or Professor Ron Knott, e.g., <https://r-knott.surrey.ac.uk/Fibonacci/cfINTRO.html> .
	"""
	
	cran = "contFracR" 

	version("1.2.1", md5="fc19411e5cc7fbc7c95b7b6c36156492")

	depends_on("r-rmpfr", type=("build", "run"))
	depends_on("r-go2bigq", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
