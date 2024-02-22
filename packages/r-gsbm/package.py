# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsbm(RPackage):
	"""Estimate Parameters in the Generalized SBM

	Given an adjacency matrix drawn from a Generalized Stochastic Block Model with missing observations, this package robustly estimates the probabilities of connection between nodes and detects outliers nodes, as describes in Gaucher, Klopp and Robin (2019) <arXiv:1911.13122>.
	"""
	
	cran = "gsbm" 

	version("0.2.2", md5="44bfea1f1beee6438d5a68d63dcdef20")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-softimpute", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
