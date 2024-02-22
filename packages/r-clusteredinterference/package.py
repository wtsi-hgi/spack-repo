# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClusteredinterference(RPackage):
	"""Causal Effects from Observational Studies with Clustered
Interference

	Estimating causal effects from observational studies assuming 
    clustered (or partial) interference. These inverse probability-weighted
    estimators target new estimands arising from population-level treatment 
    policies. The estimands and estimators are introduced in Barkley et al. 
    (2017) <arXiv:1711.04834>.
	"""
	
	homepage = "http://github.com/BarkleyBG/clusteredinterference"
	cran = "clusteredinterference" 

	version("1.0.1", md5="24471dc34c234d1c031d80909e380fd6")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-formula@1.1.2:", type=("build", "run"))
	depends_on("r-cubature@1.1.2:", type=("build", "run"))
	depends_on("r-lme4@1.1.10:", type=("build", "run"))
	depends_on("r-numderiv@2014.2.1:", type=("build", "run"))
	depends_on("r-rootsolve@1.6.6:", type=("build", "run"))
