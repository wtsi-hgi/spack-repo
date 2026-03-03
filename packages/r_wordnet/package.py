# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWordnet(RPackage):
	"""WordNet Interface

	An interface to WordNet using the Jawbone Java API to WordNet.
  WordNet (<https://wordnet.princeton.edu/>) is a large lexical database of
  English.  Nouns, verbs, adjectives and adverbs are grouped into sets of
  cognitive synonyms (synsets), each expressing a distinct concept.  Synsets
  are interlinked by means of conceptual-semantic and lexical relations.
  Please note that WordNet(R) is a registered tradename.  Princeton
  University makes WordNet available to research and commercial users
  free of charge provided the terms of their license
  (<https://wordnet.princeton.edu/license-and-commercial-use>) are followed,
  and proper reference is made to the project using an appropriate
  citation (<https://wordnet.princeton.edu/citing-wordnet>).
	"""
	
	homepage = "https://wordnet.princeton.edu/"
	cran = "wordnet" 

	version("0.1-16", md5="043a4b35b4158c74de4dc6de5155ce68")

	depends_on("r-rjava@0.6.3:", type=("build", "run"))
	depends_on("openjdk@1.5:", type=("build", "link", "run"))
	depends_on("wordnet", type=("build", "link", "run"))
