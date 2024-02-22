# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicroclass(RPackage):
	"""Methods for Taxonomic Classification of Prokaryotes

	Functions for assigning 16S sequence data to a
    taxonomic level in the tree-of-life for prokaryotes.
	"""
	
	cran = "microclass" 

	version("1.2", md5="4440040a9182e1b5d5b040c71506e4c0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-microseq", type=("build", "run"))
	depends_on("r-microcontax", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcpp@0.11.1:", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
