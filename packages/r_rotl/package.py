# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRotl(RPackage):
	"""Interface to the 'Open Tree of Life' API

	An interface to the 'Open Tree of Life' API to retrieve
    phylogenetic trees, information about studies used to assemble the
    synthetic tree, and utilities to match taxonomic names to 'Open Tree
    identifiers'. The 'Open Tree of Life' aims at assembling a
    comprehensive phylogenetic tree for all named species.
	"""
	
	homepage = "https://docs.ropensci.org/rotl/"
	cran = "rotl" 

	version("3.1.0", md5="15828a59a993b80d864c0129ddd04041")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-curl@3:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rentrez", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rncl@0.6:", type=("build", "run"))
