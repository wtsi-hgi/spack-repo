# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrossmap(RPackage):
	"""Apply Functions to All Combinations of List Elements

	Provides an extension to the 'purrr' family of mapping
    functions to apply a function to each combination of elements in a
    list of inputs.  Also includes functions for automatically detecting
    output type in mapping functions, finding every combination of
    elements of lists or rows of data frames, and applying multiple models
    to multiple subsets of a dataset.
	"""
	
	homepage = "https://crossmap.rossellhayes.com"
	cran = "crossmap" 

	version("0.4.0", md5="5aa5b93969d1d7ed716c2cc90e14b877")

	depends_on("r-backports", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
