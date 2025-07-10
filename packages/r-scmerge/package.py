# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScmerge(RPackage):
	"""scMerge: Merging multiple batches of scRNA-seq data

	Like all gene expression data, single-cell data suffers from batch effects and other unwanted variations that makes accurate biological interpretations difficult. The scMerge method leverages factor analysis, stably expressed genes (SEGs) and (pseudo-) replicates to remove unwanted variations and merge multiple single-cell data. This package contains all the necessary functions in the scMerge pipeline, including the identification of SEGs, replication-identification methods, and merging of single-cell data.
	"""
	
	homepage = "https://github.com/SydneyBioX/scMerge"
	bioc = "scMerge" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/scMerge_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/scMerge/scMerge_1.18.0.tar.gz"]

	version("1.18.0", sha256="843f5be76d286c63eeb0c4f06c34c7cd75765904adce97c01c0c02f07549aac8")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-biocsingular", type=("build", "run"))
	depends_on("r-biocneighbors", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-delayedmatrixstats", type=("build", "run"))
	depends_on("r-distr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-m3drop@1.9.4:", type=("build", "run"))
	depends_on("r-proxyc", type=("build", "run"))
	depends_on("r-ruv", type=("build", "run"))
	depends_on("r-cvtools", type=("build", "run"))
	depends_on("r-scater", type=("build", "run"))
	depends_on("r-batchelor", type=("build", "run"))
	depends_on("r-scran", type=("build", "run"))
	depends_on("r-s4vectors@0.23.19:", type=("build", "run"))
	depends_on("r-singlecellexperiment@1.7.3:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
