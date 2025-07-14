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

	version("1.28.0", commit="2f84662df9cfa5dbcadfabcdf99c5ce1924aaa60")
	version("1.22.0", commit="d9163f41536535addacdf4b7df80f10386c457f4")

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
