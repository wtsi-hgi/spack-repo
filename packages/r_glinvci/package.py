# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlinvci(RPackage):
	"""Phylogenetic Comparative Methods with Uncertainty Estimates

	A framework for analytically computing the asymptotic confidence intervals and maximum-likelihood estimates of a class of continuous-time Gaussian branching processes defined by Mitov V, Bartoszek K, Asimomitis G, Stadler T (2019) <doi:10.1016/j.tpb.2019.11.005>. The class of model includes the widely used Ornstein-Uhlenbeck and Brownian motion branching processes. The framework is designed to be flexible enough so that the users can easily specify their own sub-models, or re-parameterizations, and obtain the maximum-likelihood estimates and confidence intervals of their own custom models.
	"""
	
	homepage = "https://git.sr.ht/~hckiang/glinvci"
	cran = "glinvci" 

	version("1.2.2", md5="37536d7df463f080dbb9a87d5d782d08")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-lbfgsb3c", type=("build", "run"))
	depends_on("r-bb", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
