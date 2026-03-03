# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPst(RPackage):
	"""Probabilistic Suffix Trees and Variable Length Markov Chains

	Provides a framework for analysing state sequences with probabilistic suffix trees (PST), the construction that stores variable length Markov chains (VLMC). Besides functions for learning and optimizing VLMC models, the PST library includes many additional tools to analyse sequence data with these models: visualization tools, functions for sequence prediction and artificial sequences generation, as well as for context and pattern mining. The package is specifically adapted to the field of social sciences by allowing to learn VLMC models from sets of individual sequences possibly containing missing values, and by accounting for case weights. The  library also allows to compute probabilistic divergence between two models, and to fit segmented VLMC, where sub-models fitted to distinct strata of the learning sample are stored in a single PST. This software results from research work executed within the framework of the Swiss National Centre of Competence in Research LIVES, which is financed by the Swiss National Science Foundation. The authors are grateful to the Swiss National Science Foundation for its financial support.
	"""
	
	homepage = "https://r-forge.r-project.org/projects/pst"
	cran = "PST" 

	version("0.94.1", md5="48ab852c42663a5d88b23ca2b0aec3c4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-traminer", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
