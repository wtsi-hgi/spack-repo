# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMbkmeans(RPackage):
	"""Mini-batch K-means Clustering for Single-Cell RNA-seq

	Implements the mini-batch k-means algorithm for large datasets, including support for on-disk data representation.
	"""
	
	bioc = "mbkmeans" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/mbkmeans_1.18.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/mbkmeans/mbkmeans_1.18.0.tar.gz"]

	version("1.18.0", md5="1bd55f0f927fea250caa1a8264e3013c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-clusterr", type=("build", "run"))
	depends_on("r-benchmarkme", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.7.2:", type=("build", "run"))
	depends_on("r-rhdf5lib", type=("build", "run"))
	depends_on("r-beachmat", type=("build", "run"))
