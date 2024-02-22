# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSbicgraph(RPackage):
	"""Structural Bayesian Information Criterion for Graphical Models

	This is the implementation of the novel structural Bayesian information criterion by Zhou, 2020 (under review).
   In this method, the prior structure is modeled and incorporated into the Bayesian information criterion framework. 
   Additionally, we also provide the implementation of a two-step algorithm to generate the candidate model pool.
	"""
	
	cran = "SBICgraph" 

	version("1.0.0", md5="b4e37acede8724d05dceb7224a626a2b")

	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
