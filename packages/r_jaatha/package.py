# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJaatha(RPackage):
	"""Simulation-Based Maximum Likelihood Parameter Estimation

	An estimation method that can use computer simulations to
    approximate maximum-likelihood estimates even when the likelihood function can not
    be evaluated directly. It can be applied whenever it is feasible to conduct many
    simulations, but works best when the data is approximately Poisson distributed.
    It was originally designed for demographic inference in evolutionary
    biology (Naduvilezhath et al., 2011 <doi:10.1111/j.1365-294X.2011.05131.x>,
    Mathew et al., 2013 <doi:10.1002/ece3.722>).
    It has optional support for conducting coalescent simulation using
    the 'coala' package.
	"""
	
	homepage = "https://github.com/statgenlmu/jaatha"
	cran = "jaatha" 

	version("3.2.5", md5="503108aa45f8dbee0b5437bd3f17daca")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-assertthat@0.1:", type=("build", "run"))
	depends_on("r-r6@2.1.1:", type=("build", "run"))
