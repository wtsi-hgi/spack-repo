# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNimblenobounds(RPackage):
	"""Transformed Distributions for Improved MCMC Efficiency

	A collection of common univariate bounded probability distributions transformed to the unbounded real line, for the purpose of increased MCMC efficiency.
	"""
	
	homepage = "https://github.com/DRJP/nimbleNoBounds"
	cran = "nimbleNoBounds" 

	version("1.0.2", md5="e6cb61cea62148f8c23dc2dac36b770a")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-nimble", type=("build", "run"))
