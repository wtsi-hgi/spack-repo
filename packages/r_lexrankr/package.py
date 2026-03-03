# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLexrankr(RPackage):
	"""Extractive Summarization of Text with the LexRank Algorithm

	An R implementation of the LexRank algorithm described by G. Erkan and D. R. Radev (2004) <DOI:10.1613/jair.1523>.
	"""
	
	homepage = "https://github.com/AdamSpannbauer/lexRankr/"
	cran = "lexRankr" 

	version("0.5.2", md5="9c5f4bdf13271e2c665860a042bcd4c0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-snowballc", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
