# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRprime(RPackage):
	"""Functions for Working with 'Eprime' Text Files

	'Eprime' is a set of programs for administering
    psychological experiments by computer. This package provides functions
    for loading, parsing, filtering and exporting data in the text files
    produced by 'Eprime' experiments.
	"""
	
	homepage = "https://github.com/tjmahr/rprime"
	cran = "rprime" 

	version("0.1.2", md5="42a3524ca9cbf743869393d5b591d441")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr@1:", type=("build", "run"))
