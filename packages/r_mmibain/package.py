# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmibain(RPackage):
	"""Bayesian Informative Hypotheses Evaluation Web Applications

	Researchers often have expectations about the relations between means
    of different groups or standardized regression coefficients; using informative
    hypothesis testing to incorporate these expectations into the analysis through
    order constraints increases statistical power
    Vanbrabant and Rosseel (2020) <doi:10.4324/9780429273872-14>. Another valuable
    tool, the Bayes factor, can evaluate evidence for multiple hypotheses without
    concerns about multiple testing, and can be used in Bayesian updating
    Hoijtink, Mulder, van Lissa & Gu (2019) <doi:10.1037/met0000201>. The 'bain'
    R package enables informative hypothesis testing using the Bayes factor. The
    'mmibain' package provides 'shiny' web applications based on 'bain'. The
    RepliCrisis() function launches a 'shiny' card game to simulate the evaluation
    of replication studies while the mmibain() function launches a 'shiny'
    application to fit Bayesian informative hypotheses evaluation models from
    'bain'.
	"""
	
	homepage = "https://github.com/mightymetrika/mmibain"
	cran = "mmibain" 

	version("0.1.1", md5="bee4d549ea67b6dbaa0c4f23cb9cb902")

	depends_on("r-bain", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-mmcards", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
