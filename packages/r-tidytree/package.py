# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidytree(RPackage):
	"""A Tidy Tool for Phylogenetic Tree Data Manipulation.

	Phylogenetic tree generally contains multiple components including node,
	edge, branch and associated data. 'tidytree' provides an approach to
	convert tree object to tidy data frame as well as provides tidy interfaces
	to manipulate tree data."""

	cran = "tidytree"

	license("Artistic-2.0")

	version("0.4.6", md5="0b27b0d945a7fb845ca9d8d1d57a1d2b")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-yulab-utils@0.0.4:", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
