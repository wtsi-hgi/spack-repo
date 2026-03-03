# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStopwords(RPackage):
	"""Multilingual Stopword Lists

	Provides multiple sources of stopwords, for use in text analysis and natural language processing.
	"""
	
	homepage = "https://github.com/quanteda/stopwords"
	cran = "stopwords" 

	version("2.3", md5="91b96c7bee56e9c6fc6a6945cfc47a67")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-isocodes", type=("build", "run"))
