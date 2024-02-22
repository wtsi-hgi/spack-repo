# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCleannlp(RPackage):
	"""A Tidy Data Model for Natural Language Processing

	Provides a set of fast tools for converting a textual corpus into
  a set of normalized tables. Users may make use of the 'udpipe' back end with
  no external dependencies, or two Python back ends with 'spaCy'
  <https://spacy.io> or 'CoreNLP' <https://stanfordnlp.github.io/CoreNLP/>.
  Exposed annotation tasks include tokenization, part of speech tagging, named
  entity recognition, and dependency parsing.
	"""
	
	homepage = "https://statsmaths.github.io/cleanNLP/"
	cran = "cleanNLP" 

	version("3.0.7", md5="e709280a0ab9ccd463bef3a1ddd92d72")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix@1.2:", type=("build", "run"))
	depends_on("r-udpipe", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("python@3.7:", type=("build", "link", "run"))
