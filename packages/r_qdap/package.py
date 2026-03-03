# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQdap(RPackage):
	"""Bridging the Gap Between Qualitative Data and Quantitative
Analysis

	Automates many of the tasks associated with quantitative discourse analysis of transcripts containing discourse
              including frequency counts of sentence types, words, sentences, turns of talk, syllables and other assorted
              analysis tasks. The package provides parsing tools for preparing transcript data. Many functions enable the user
              to aggregate data by any number of grouping variables, providing analysis and seamless integration with other R
              packages that undertake higher level analysis and visualization of text. This affords the user a more efficient
              and targeted analysis. 'qdap' is designed for transcript analysis, however, many functions are applicable to other
              areas of Text Mining/ Natural Language Processing.
	"""
	
	homepage = "https://trinker.github.io/qdap/"
	cran = "qdap" 

	version("2.4.6", md5="9da41754468a0d23a28fc52432737647")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-qdapdictionaries@1.0.2:", type=("build", "run"))
	depends_on("r-qdapregex@0.1.2:", type=("build", "run"))
	depends_on("r-qdaptools@1.3.1:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-chron", type=("build", "run"))
	depends_on("r-dplyr@0.3:", type=("build", "run"))
	depends_on("r-gender@0.5.1:", type=("build", "run"))
	depends_on("r-ggplot2@2.1:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-nlp", type=("build", "run"))
	depends_on("r-opennlp@0.2.1:", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tm@0.7.6:", type=("build", "run"))
	depends_on("r-venneuler", type=("build", "run"))
	depends_on("r-wordcloud", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
