# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsychwordvec(RPackage):
	"""Word Embedding Research Framework for Psychological Science

	
    An integrative toolbox of word embedding research that provides:
    (1) a collection of 'pre-trained' static word vectors in the '.RData'
    compressed format <https://psychbruce.github.io/WordVector_RData.pdf>;
    (2) a series of functions to process, analyze, and visualize word vectors;
    (3) a range of tests to examine conceptual associations, including
    the Word Embedding Association Test <doi:10.1126/science.aal4230>
    and the Relative Norm Distance <doi:10.1073/pnas.1720347115>,
    with permutation test of significance;
    (4) a set of training methods to locally train (static) word vectors
    from text corpora, including 'Word2Vec' <arXiv:1301.3781>,
    'GloVe' <doi:10.3115/v1/D14-1162>, and 'FastText' <arXiv:1607.04606>;
    (5) a group of functions to download 'pre-trained' language models
    (e.g., 'GPT', 'BERT') and extract contextualized (dynamic) word vectors
    (based on the R package 'text').
	"""
	
	homepage = "https://psychbruce.github.io/PsychWordVec/"
	cran = "PsychWordVec" 

	version("2023.9", md5="d4aafbe287acf4b10791e15785bb044f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-brucer", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-vroom", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-qgraph", type=("build", "run"))
	depends_on("r-rsparse", type=("build", "run"))
	depends_on("r-text2vec", type=("build", "run"))
	depends_on("r-word2vec", type=("build", "run"))
	depends_on("r-fasttextr", type=("build", "run"))
	depends_on("r-text", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
