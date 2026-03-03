# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSld(RPackage):
	"""Estimation and Use of the Quantile-Based Skew Logistic
Distribution

	The skew logistic distribution is a quantile-defined generalisation
 of the logistic distribution (van Staden and King 2015).  Provides random 
 numbers, quantiles, probabilities, densities and density quantiles for the distribution.
 It provides Quantile-Quantile plots and method of L-Moments estimation 
 (including asymptotic standard errors) for the distribution.
	"""
	
	homepage = "https://github.com/newystats/SLD/"
	cran = "sld" 

	version("1.0.1", md5="6838b4d637835d3416c3aa6353d6a984")

	depends_on("r-lmom", type=("build", "run"))
