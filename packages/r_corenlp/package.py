# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorenlp(RPackage):
	"""Wrappers Around Stanford CoreNLP Tools

	Provides a minimal interface for applying
    annotators from the 'Stanford CoreNLP' java library. Methods
    are provided for tasks such as tokenisation, part of speech
    tagging, lemmatisation, named entity recognition, coreference
    detection and sentiment analysis.
	"""
	
	cran = "coreNLP" 

	version("0.4-3", md5="b01a65c073f6af56724cc7aa9011afca")

	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("openjdk@1.7:", type=("build", "link", "run"))
