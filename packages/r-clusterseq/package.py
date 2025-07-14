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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/clusterSeq_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/clusterSeq/clusterSeq_1.26.0.tar.gz"]

	version("1.32.0", tag="RELEASE_3_21")
	version("1.26.0", sha256="6ed3a2ae16abd36fc8dc17e6877ab39ded1193e7cebe83fb836f65101af3893a")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-bayseq", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
