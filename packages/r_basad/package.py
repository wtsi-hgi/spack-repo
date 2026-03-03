# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBasad(RPackage):
	"""Bayesian Variable Selection with Shrinking and Diffusing Priors

	Provides a Bayesian variable selection approach using continuous spike and slab prior distributions. The prior choices here are motivated by the shrinking and diffusing priors studied in Narisetty & He (2014) <DOI:10.1214/14-AOS1207>.
	"""
	
	cran = "basad" 

	version("0.3.0", md5="0dff12c6da2ebecef17a8afc47e6314c")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rmutil", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
