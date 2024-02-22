# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWordsalad(RPackage):
	"""Provide Tools to Extract and Analyze Word Vectors

	Provides access to various word embedding methods (GloVe, 
    fasttext and word2vec) to extract word vectors using a unified framework to
    increase reproducibility and correctness.
	"""
	
	homepage = "https://github.com/EmilHvitfeldt/wordsalad"
	cran = "wordsalad" 

	version("0.2.0", md5="5b308474e1632e82ecfd4f0f94d6a112")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-text2vec", type=("build", "run"))
	depends_on("r-word2vec", type=("build", "run"))
	depends_on("r-fasttextr", type=("build", "run"))
