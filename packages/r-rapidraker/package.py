# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRapidraker(RPackage):
	"""Rapid Automatic Keyword Extraction (RAKE) Algorithm

	A 'Java' implementation of the RAKE algorithm ('Rose', S., 'Engel', D., 
  'Cramer', N. and 'Cowley', W. (2010) <doi:10.1002/9780470689646.ch1>), which can 
  be used to extract keywords from documents without any training data.
	"""
	
	homepage = "https://crew102.github.io/slowraker/articles/rapidraker.html"
	cran = "rapidraker" 

	version("0.1.3", md5="010c206dd3dea811c7399b4c2d8b80c6")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-opennlpdata", type=("build", "run"))
	depends_on("r-slowraker", type=("build", "run"))
	depends_on("openjdk@8:", type=("build", "link", "run"))
