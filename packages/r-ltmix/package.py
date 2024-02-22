# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLtmix(RPackage):
	"""Left-Truncated Mixtures of Gamma, Weibull, and Lognormal
Distributions

	Mixture modelling of one-dimensional data using combinations of left-truncated Gamma, Weibull, and Lognormal Distributions. Blostein, Martin & Miljkovic, Tatjana. (2019) <doi:10.1016/j.insmatheco.2018.12.001>. 
	"""
	
	cran = "ltmix" 

	version("0.2.1", md5="079c8f5071c5fdee64b860610856278d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
