# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIloreg(RPackage):
	"""ILoReg: a tool for high-resolution cell population identification from scRNA-Seq data

	ILoReg is a tool for identification of cell populations from scRNA-seq data. In particular, ILoReg is useful for finding cell populations with subtle transcriptomic differences. The method utilizes a self-supervised learning method, called Iteratitive Clustering Projection (ICP), to find cluster probabilities, which are used in noise reduction prior to PCA and the subsequent hierarchical clustering and t-SNE steps. Additionally, functions for differential expression analysis to find gene markers for the populations and gene expression visualization are provided.
	"""
	
	homepage = "https://github.com/elolab/ILoReg"
	bioc = "ILoReg" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ILoReg_1.12.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ILoReg/ILoReg_1.12.1.tar.gz"]

	version("1.18.0", tag="RELEASE_3_21")
	version("1.12.1", sha256="ed5ac78d1139c9aa3d97795b257b0f517804678266eca928e80f463779f6d878")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-aricode", type=("build", "run"))
	depends_on("r-liblinear", type=("build", "run"))
	depends_on("r-sparsem", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-umap", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-fastcluster", type=("build", "run"))
	depends_on("r-paralleldist", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
