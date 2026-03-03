# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHbbr(RPackage):
	"""Hierarchical Bayesian Benefit-Risk Assessment Using Discrete
Choice Experiment

	Implements assessment of benefit-risk balance using Bayesian Discrete Choice Experiment. For more details see the article by Mukhopadhyay et al. (2019) <DOI:10.1080/19466315.2018.1527248>. 
	"""
	
	cran = "hbbr" 

	version("1.1.2", md5="c1ff64a15161c29f02343ad16b8913ee")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-r2jags", type=("build", "run"))
