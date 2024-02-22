# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesmix(RPackage):
	"""Bayesian Mixture Models with JAGS

	Fits finite mixture models of univariate Gaussian distributions using JAGS within a Bayesian framework.
	"""
	
	homepage = "https://statmath.wu.ac.at/~gruen/BayesMix/"
	cran = "bayesmix" 

	version("0.7-6", md5="1e3102697727673606f1e33905a245a2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rjags@2.1:", type=("build", "run"))
	depends_on("r-coda@0.13:", type=("build", "run"))
