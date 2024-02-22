# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDicer(RPackage):
	"""Diverse Cluster Ensemble in R

	Performs cluster analysis using an ensemble clustering
    framework, Chiu & Talhouk (2018) <doi:10.1186/s12859-017-1996-y>.
    Results from a diverse set of algorithms are pooled together using
    methods such as majority voting, K-Modes, LinkCluE, and CSPA. There
    are options to compare cluster assignments across algorithms using
    internal and external indices, visualizations such as heatmaps, and
    significance testing for the existence of clusters.
	"""
	
	homepage = "https://github.com/AlineTalhouk/diceR/"
	cran = "diceR" 

	version("2.2.0", md5="129a82879f63326d58087b0cbd5edd27")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-clue", type=("build", "run"))
	depends_on("r-clustersim", type=("build", "run"))
	depends_on("r-clv", type=("build", "run"))
	depends_on("r-clvalid", type=("build", "run"))
	depends_on("r-dplyr@0.7.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-infotheo", type=("build", "run"))
	depends_on("r-klar", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-nmf", type=("build", "run"))
	depends_on("r-purrr@0.2.3:", type=("build", "run"))
	depends_on("r-rankaggreg", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-yardstick", type=("build", "run"))
