# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNpistats(RPackage):
	"""Nonparametric Predictive Inference

	An implementation of the Nonparametric Predictive Inference approach in R. It provides tools for quantifying uncertainty via lower and upper probabilities. It includes useful functions for pairwise and multiple comparisons: comparing two groups with and without terminated tails, selecting the best group, selecting the subset of best groups, selecting the subset including the best group.
	"""
	
	cran = "NPIstats" 

	version("0.1.0", md5="7876caeaf6c753403bf950409f719527")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
