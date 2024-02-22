# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModesto(RPackage):
	"""Modeling and Analysis of Stochastic Systems

	Compute important quantities when we consider stochastic systems that are observed continuously. 
             Such as, Cost model, Limiting distribution, Transition matrix, Transition distribution and Occupancy matrix. 
             The methods are described, for example, Ross S. (2014), Introduction to Probability Models. Eleven Edition. Academic Press. 
	"""
	
	cran = "modesto" 

	version("0.1.4", md5="a7720357f2e5549ffd4946d51bd75991")

	depends_on("r-markovchain", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
