# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpennlp(RPackage):
	"""Apache OpenNLP Tools Interface

	An interface to the Apache OpenNLP tools (version 1.5.3).
  The Apache OpenNLP library is a machine learning based toolkit for the
  processing of natural language text written in Java.
  It supports the most common NLP tasks, such as tokenization, sentence
  segmentation, part-of-speech tagging, named entity extraction, chunking,
  parsing, and coreference resolution.
  See <https://opennlp.apache.org/> for more information.
	"""
	
	cran = "openNLP" 

	version("0.2-7", md5="09e7291bd53b8840113cca6c700789b1")

	depends_on("r-nlp@0.1.6.3:", type=("build", "run"))
	depends_on("r-opennlpdata@1.5.3.1:", type=("build", "run"))
	depends_on("r-rjava@0.6.3:", type=("build", "run"))
	depends_on("openjdk@5:", type=("build", "link", "run"))
