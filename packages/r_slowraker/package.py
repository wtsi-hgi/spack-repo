# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlowraker(RPackage):
	"""A Slow Version of the Rapid Automatic Keyword Extraction (RAKE)
Algorithm

	A mostly pure-R implementation of the RAKE algorithm (Rose, S., Engel, D., Cramer, N. and Cowley, W. (2010) <doi:10.1002/9780470689646.ch1>), which can be used to extract keywords from documents without any training data.
	"""
	
	homepage = "https://crew102.github.io/slowraker/index.html"
	cran = "slowraker" 

	version("0.1.1", md5="e3d5c44a41d0ea14554cfb677250995c")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-snowballc", type=("build", "run"))
	depends_on("r-nlp", type=("build", "run"))
	depends_on("r-opennlp", type=("build", "run"))
	depends_on("openjdk@5:", type=("build", "link", "run"))
