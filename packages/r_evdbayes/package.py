# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvdbayes(RPackage):
	"""Bayesian Analysis in Extreme Value Theory

	Provides functions for the Bayesian analysis of extreme
        value models, using Markov chain Monte Carlo methods. Allows
		the construction of both uninformative and informed prior 
		distributions for common statistical models applied to extreme
        event data, including the generalized extreme value distribution.		
	"""
	
	cran = "evdbayes" 

	version("1.1-3", md5="c6601f14dd70f9b30d479bb25ae970b2")

	depends_on("r@1.8:", type=("build", "run"))
