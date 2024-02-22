# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreeio(RPackage):
	"""Base Classes and Functions for Phylogenetic Tree Input and Output.

	'treeio' is an R package to make it easier to import and store phylogenetic
	tree with associated data; and to link external data from different sources
	to phylogeny. It also supports exporting phylogenetic tree with
	heterogeneous associated data to a single tree file and can be served as a
	platform for merging tree with associated data and converting file
	formats."""

	bioc = "treeio"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/treeio_1.26.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/treeio/treeio_1.26.0.tar.gz"]

	version("1.26.0", md5="583758f88bf0d8efa0749407f4183567")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidytree@0.4.5:", type=("build", "run"))
