# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidystopwords(RPackage):
	"""Customisable Stop-Words in 110 Languages

	Functions to generate stop-word lists in 110 languages, in a way consistent across all the languages supported. The generated lists are based on the morphological tagset from the Universal Dependencies.
	"""
	
	cran = "tidystopwords" 

	version("0.9.1", md5="b45ab5c8465af17d72968f448408d146")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
