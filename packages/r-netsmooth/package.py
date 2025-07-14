# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetsmooth(RPackage):
	"""Network smoothing for scRNAseq

	netSmooth is an R package for network smoothing of single cell RNA sequencing data. Using bio networks such as protein-protein interactions as priors for gene co-expression, netsmooth improves cell type identification from noisy, sparse scRNAseq data.
	"""
	
	homepage = "https://github.com/BIMSBbioinfo/netSmooth"
	bioc = "netSmooth" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/netSmooth_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/netSmooth/netSmooth_1.22.0.tar.gz"]

	version("1.28.0", tag="RELEASE_3_21")
	version("1.22.0", sha256="945bef784c08479b7bdf08f55c0e4b6f112355e0f900d767313c709566bf72f2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-scater@1.15.11:", type=("build", "run"))
	depends_on("r-clusterexperiment@2.1.6:", type=("build", "run"))
	depends_on("r-entropy", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-hdf5array@1.15.13:", type=("build", "run"))
