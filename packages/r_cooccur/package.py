# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCooccur(RPackage):
	"""Probabilistic Species Co-Occurrence Analysis in R

	This R package applies the probabilistic model of species co-occurrence (Veech 2013) to a set of species distributed among a set of survey or sampling sites. The algorithm calculates the observed and expected frequencies of co-occurrence between each pair of species. The expected frequency is based on the distribution of each species being random and independent of the other species. The analysis returns the probabilities that a more extreme (either low or high) value of co-occurrence could have been obtained by chance. The package also includes functions for visualizing species co-occurrence results and preparing data for downstream analyses.
	"""
	
	cran = "cooccur" 

	version("1.3", md5="f21506562eda5110d9fd477a58d76608")

	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
