# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlpclient(RPackage):
	"""Stanford 'CoreNLP' Annotation Client

	Stanford 'CoreNLP' annotation client.
  Stanford 'CoreNLP' <https://stanfordnlp.github.io/CoreNLP/index.html> integrates all 
  NLP tools from the Stanford Natural Language Processing Group, 
  including a part-of-speech (POS) tagger, a named entity recognizer (NER), 
  a parser, and a coreference resolution system, and provides model files 
  for the analysis of English. More information can be found in the README.
	"""
	
	cran = "NLPclient" 

	version("1.0", md5="fd9289004c70dce307712df35650f275")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-nlp@0.1.10:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
