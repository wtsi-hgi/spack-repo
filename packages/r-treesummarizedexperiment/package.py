# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreesummarizedexperiment(RPackage):
	"""TreeSummarizedExperiment: a S4 Class for Data with Tree Structures

	TreeSummarizedExperiment has extended SingleCellExperiment to include hierarchical information on the rows or columns of the rectangular data.
	"""
	
	bioc = "TreeSummarizedExperiment"

	version("2.16.1", commit="f3efa55a10d78c40211ec3bbc94dfd463018a407")
	version("2.10.0", commit="71a273a9d46a3e62be26d62b25ca822eccb3aad8")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-s4vectors@0.23.18:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-treeio", type=("build", "run"))
