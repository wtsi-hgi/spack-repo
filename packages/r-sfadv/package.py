# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSfadv(RPackage):
	"""Advanced Methods for Stochastic Frontier Analysis

	
 Stochastic frontier analysis with advanced methods.
 In particular, it applies the approach proposed by Latruffe et al. (2017) 
 <DOI:10.1093/ajae/aaw077> to estimate a stochastic frontier with technical 
 inefficiency effects when one input is endogenous.
	"""
	
	cran = "sfadv" 

	version("1.0.1", md5="58833b59c3703471206730d37c61735f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-gmm", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
