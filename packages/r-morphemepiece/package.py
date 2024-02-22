# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMorphemepiece(RPackage):
	"""Morpheme Tokenization

	Tokenize text into morphemes. The morphemepiece algorithm uses a 
  lookup table to determine the morpheme breakdown of words, and falls back on a 
  modified wordpiece tokenization algorithm for words not found in the lookup 
  table.
	"""
	
	homepage = "https://github.com/macmillancontentscience/morphemepiece"
	cran = "morphemepiece" 

	version("1.2.3", md5="7c58a2eff309e8f08a427abd888b031d")

	depends_on("r-dlr@1:", type=("build", "run"))
	depends_on("r-fastmatch", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-memoise@2:", type=("build", "run"))
	depends_on("r-morphemepiece-data", type=("build", "run"))
	depends_on("r-piecemaker@1:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
