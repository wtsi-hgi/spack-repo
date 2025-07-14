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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/TreeSummarizedExperiment_2.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/TreeSummarizedExperiment/TreeSummarizedExperiment_2.10.0.tar.gz"]

    version("2.16.1", tag="RELEASE_3_21")
	version("2.10.0", sha256="cf7cd38f3199dc9324b6dbedd40ce2fae4c910abd0b11c41d7eaaa1d698f78fb")

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
