# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsentiment(RPackage):
	"""Analyse Sentiment of English Sentences

	Analyses sentiment of a sentence in English and assigns score to it. It can classify sentences to the following categories of sentiments:- Positive, Negative, very Positive, very negative, 
              Neutral. For a vector of sentences, it counts the number of sentences in each
              category of sentiment.In calculating the score, negation and various degrees
              of adjectives are taken into consideration. It deals only with English sentences.
	"""
	
	cran = "RSentiment" 

	version("2.2.2", md5="78c24dfa018cc695cac6c79d846e7a56")

	depends_on("r@2.1:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-opennlp", type=("build", "run"))
	depends_on("r-nlp", type=("build", "run"))
