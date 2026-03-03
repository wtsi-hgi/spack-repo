# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCctpack(RPackage):
	"""Consensus Analysis, Model-Based Clustering, and Cultural
Consensus Theory Applications

	Consensus analysis, model-based clustering, and cultural consensus theory applications to response data (e.g. questionnaires). The models are applied using hierarchical Bayesian inference. The current package version supports binary, ordinal, and continuous data formats. 
	"""
	
	cran = "CCTpack" 

	version("1.5.2", md5="dacb14a147febe77a3512026cafbf4cf")

	depends_on("r-r2jags@0.4.03:", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-polycor", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
