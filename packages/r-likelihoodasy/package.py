# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLikelihoodasy(RPackage):
	"""Functions for Likelihood Asymptotics

	Functions for computing the r and r* statistics for inference on an arbitrary scalar function of model parameters, plus some code for the (modified) profile likelihood.
	"""
	
	cran = "likelihoodAsy" 

	version("0.51", md5="c161e4d3b33c09ed7678c91995719989")

	depends_on("r-cond", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-alabama", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
