# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClusterseq(RPackage):
	"""Clustering of high-throughput sequencing data by identifying co-expression patterns

	Identification of clusters of co-expressed genes based on their expression across multiple (replicated) biological samples.
	"""
	
	bioc = "clusterSeq" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/clusterSeq_1.26.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/clusterSeq/clusterSeq_1.26.0.tar.gz"]

	version("1.26.0", md5="c0f51fc6b851b707de4f53107c6179f5")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-bayseq", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
