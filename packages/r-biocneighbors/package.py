# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiocneighbors(RPackage):
	"""Nearest Neighbor Detection for Bioconductor Packages.

	Implements exact and approximate methods for nearest neighbor detection,
	in a framework that allows them to be easily switched within
	Bioconductor packages or workflows. Exact searches can be performed
	using the k-means for k-nearest neighbors algorithm or with vantage
	point trees. Approximate searches can be performed using the Annoy or
	HNSW libraries. Searching on either Euclidean or Manhattan distances is
	supported. Parallelization is achieved for all methods by using
	BiocParallel. Functions are also provided to search for all neighbors
	within a given distance."""

	bioc = "BiocNeighbors"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/BiocNeighbors_1.20.2.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/BiocNeighbors/BiocNeighbors_1.20.2.tar.gz"]

	version("1.20.2", md5="60f1ea60fb00cfd92dfa247765da9204")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpphnsw", type=("build", "run"))
