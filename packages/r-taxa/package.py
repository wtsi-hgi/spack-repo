# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTaxa(RPackage):
	"""Classes for Storing and Manipulating Taxonomic Data

	Provides classes for storing and manipulating taxonomic data. 
 Most of the classes can be treated like base R vectors (e.g. can be used 
 in tables as columns and can be named). Vectorized classes can store taxon names
 and authorities, taxon IDs from databases, taxon ranks, and other types of
 information. More complex classes are provided to store taxonomic trees and
 user-defined data associated with them.
	"""
	
	homepage = "https://docs.ropensci.org/taxa/"
	cran = "taxa" 

	version("0.4.3", md5="17d5d128ff9ad77459a2c5d55ac3d2aa")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
