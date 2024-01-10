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

	version("1.18.0", commit="8b9a2dcac6431634d7ac183fa6cf98209d99c746")

	depends_on("r@3.6.0:", type=("build", "run"))
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
