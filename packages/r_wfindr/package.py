# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWfindr(RPackage):
	"""Crossword, Scrabble and Anagram Solver

	Provides a large English words list and tools to find words by patterns. In particular, anagram finder and scrabble word finder.
	"""
	
	homepage = "https://github.com/idmn/wfindr"
	cran = "wfindr" 

	version("0.1.0", md5="82ced660516f64a8b2767e7486dfae10")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
