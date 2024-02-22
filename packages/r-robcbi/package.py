# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobcbi(RPackage):
	"""Conditionally Unbiased Bounded Influence Estimates

	Conditionally unbiased bounded influence estimates as described in 
  Kuensch et al. (1989) <doi:10.1080/01621459.1989.10478791> in three special cases of 
  the generalized linear model: Bernoulli, Binomial, and Poisson distributed responses. 
	"""
	
	cran = "robcbi" 

	version("1.1-4", md5="ff0c00498eb036c393578be69b774973")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-robeth", type=("build", "run"))
