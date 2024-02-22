# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRankingproject(RPackage):
	"""The Ranking Project: Visualizations for Comparing Populations

	Functions to generate plots and tables for comparing independently-
    sampled populations. Companion package to "A Primer on Visualizations
    for Comparing Populations, Including the Issue of Overlapping Confidence
    Intervals" by Wright, Klein, and Wieczorek (2019)
    <DOI:10.1080/00031305.2017.1392359> and "A Joint Confidence Region for an
    Overall Ranking of Populations" by Klein, Wright, and Wieczorek (2020)
    <DOI:10.1111/rssc.12402>.
	"""
	
	homepage = "https://github.com/civilstat/RankingProject"
	cran = "RankingProject" 

	version("0.4.0", md5="bb39f90b21a275b5b09a0c02a69a72ab")

	depends_on("r@2.10:", type=("build", "run"))
