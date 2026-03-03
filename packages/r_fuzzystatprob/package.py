# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFuzzystatprob(RPackage):
	"""Fuzzy Stationary Probabilities from a Sequence of Observations
of an Unknown Markov Chain

	An implementation of a method for computing fuzzy numbers representing stationary probabilities of an unknown Markov chain,
        from which a sequence of observations along time has been obtained. The algorithm is based on the proposal presented by James Buckley 
        in his book on Fuzzy probabilities (Springer, 2005), chapter 6. Package 'FuzzyNumbers' is used to represent the output probabilities.
	"""
	
	homepage = "http://decsai.ugr.es/~pjvi/r-packages.html"
	cran = "FuzzyStatProb" 

	version("2.0.4", md5="dc05f31561d35266225fd1bcccbe270f")

	depends_on("r-multinomialci", type=("build", "run"))
	depends_on("r-fuzzynumbers", type=("build", "run"))
	depends_on("r-deoptim", type=("build", "run"))
