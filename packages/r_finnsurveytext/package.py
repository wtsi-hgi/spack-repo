# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFinnsurveytext(RPackage):
	"""Analyse Open-Ended Survey Responses in Finnish

	Annotates Finnish textual survey responses into CoNLL-U format using Finnish treebanks from <https://universaldependencies.org/format.html> using UDPipe as described in Straka and Straková (2017) <doi:10.18653/v1/K17-3009>. Formatted data is then analysed using single or comparison n-gram plots, wordclouds, summary tables and Concept Network plots. The Concept Network plots use the TextRank algorithm as outlined in Mihalcea, Rada & Tarau, Paul (2004) <https://aclanthology.org/W04-3252/>.
	"""
	
	homepage = "https://dariah-fi-survey-concept-network.github.io/finnsurveytext/"
	cran = "finnsurveytext" 

	version("1.0.0", md5="ed7cb032d0fa93779f868e717222b6ac")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-stopwords", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-textrank", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-udpipe", type=("build", "run"))
	depends_on("r-wordcloud", type=("build", "run"))
