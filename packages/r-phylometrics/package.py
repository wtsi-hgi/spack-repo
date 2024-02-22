# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhylometrics(RPackage):
	"""Estimating Statistical Errors of Phylogenetic Metrics

	Provides functions to estimate statistical errors of phylogenetic
    metrics particularly to detect binary trait influence on diversification, as
    well as a function to simulate trees with fixed number of sampled taxa and trait
    prevalence.
	"""
	
	cran = "phylometrics" 

	version("0.0.1", md5="05db34f3a2e9d03f37280d9004a39e10")

	depends_on("r@2.1.1:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
