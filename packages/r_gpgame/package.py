# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGpgame(RPackage):
	"""Solving Complex Game Problems using Gaussian Processes

	Sequential strategies for finding a game equilibrium are proposed in a black-box setting (expensive pay-off evaluations, no derivatives). The algorithm handles noiseless or noisy evaluations. Two acquisition functions are available. Graphical outputs can be generated automatically. V. Picheny, M. Binois, A. Habbal (2018) <doi:10.1007/s10898-018-0688-0>. M. Binois, V. Picheny, P. Taillandier, A. Habbal (2020) <arXiv:1902.06565v2>.
	"""
	
	homepage = "https://github.com/vpicheny/GPGame"
	cran = "GPGame" 

	version("1.2.0", md5="3bde493ad8e189ee9574bc714ac3227e")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dicekriging", type=("build", "run"))
	depends_on("r-gpareto", type=("build", "run"))
	depends_on("r-kriginv", type=("build", "run"))
	depends_on("r-dicedesign", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
