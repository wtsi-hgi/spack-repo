# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExperimentsubset(RPackage):
	"""Manages subsets of data with Bioconductor Experiment objects

	Experiment objects such as the SummarizedExperiment or SingleCellExperiment are data containers for one or more matrix-like assays along with the associated row and column data. Often only a subset of the original data is needed for down-stream analysis. For example, filtering out poor quality samples will require excluding some columns before analysis. The ExperimentSubset object is a container to efficiently manage different subsets of the same data without having to make separate objects for each new subset.
	"""
	
	bioc = "ExperimentSubset" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ExperimentSubset_1.12.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ExperimentSubset/ExperimentSubset_1.12.0.tar.gz"]

	version("1.12.0", md5="fc52b3d67f7f9641a3851f987af7cdee")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-spatialexperiment", type=("build", "run"))
	depends_on("r-treesummarizedexperiment", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
