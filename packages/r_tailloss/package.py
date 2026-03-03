# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTailloss(RPackage):
	"""Estimate the Probability in the Upper Tail of the Aggregate Loss
Distribution

	Set of tools to estimate the probability in the upper tail of the aggregate loss distribution using different methods: Panjer recursion, Monte Carlo simulations, Markov bound, Cantelli bound, Moment bound, and Chernoff bound.
	"""
	
	homepage = "http://github.com/igollini/tailloss"
	cran = "tailloss" 

	version("1.0", md5="ea937e8cae0aded09bb4003d1b8a8844")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
