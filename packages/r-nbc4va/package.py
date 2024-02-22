# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNbc4va(RPackage):
	"""Bayes Classifier for Verbal Autopsy Data

	An implementation of the Naive Bayes Classifier (NBC) algorithm
    used for Verbal Autopsy (VA) built on code from Miasnikof et al (2015) 
    <DOI:10.1186/s12916-015-0521-2>.
	"""
	
	cran = "nbc4va" 

	version("1.2", md5="3aab26abf4a8d6e1f0349bebb82230fc")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
