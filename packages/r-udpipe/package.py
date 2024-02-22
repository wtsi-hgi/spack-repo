# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUdpipe(RPackage):
	"""Tokenization, Parts of Speech Tagging, Lemmatization and
Dependency Parsing with the 'UDPipe' 'NLP' Toolkit

	This natural language processing toolkit provides language-agnostic
    'tokenization', 'parts of speech tagging', 'lemmatization' and 'dependency
    parsing' of raw text. Next to text parsing, the package also allows you to train
    annotation models based on data of 'treebanks' in 'CoNLL-U' format as provided
    at <https://universaldependencies.org/format.html>. The techniques are explained
    in detail in the paper: 'Tokenizing, POS Tagging, Lemmatizing and Parsing UD 2.0
    with UDPipe', available at <doi:10.18653/v1/K17-3009>. 
    The toolkit also contains functionalities for commonly used data manipulations on texts 
    which are enriched with the output of the parser. Namely functionalities and algorithms 
    for collocations, token co-occurrence, document term matrix handling, 
    term frequency inverse document frequency calculations,
    information retrieval metrics (Okapi BM25), handling of multi-word expressions,
    keyword detection (Rapid Automatic Keyword Extraction, noun phrase extraction, syntactical patterns) 
    sentiment scoring and semantic similarity analysis.
	"""
	
	homepage = "https://bnosac.github.io/udpipe/en/index.html"
	cran = "udpipe" 

	version("0.8.11", md5="f445b767c24bdb7952a8eb835ebe11e9")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table@1.9.6:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
