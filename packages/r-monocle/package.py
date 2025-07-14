# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMonocle(RPackage):
	"""Clustering, differential expression, and trajectory analysis for single- cell RNA-Seq

	Monocle performs differential expression and time-series analysis for single-cell expression experiments. It orders individual cells according to progress through a biological process, without knowing ahead of time which genes define progress through that process. Monocle also performs differential expression analysis, clustering, visualization, and other useful tasks on single cell expression data.  It is designed to work with RNA-Seq and qPCR data, but could be used with other types as well.
	"""
	
	bioc = "monocle" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/monocle_2.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/monocle/monocle_2.30.0.tar.gz"]

	version("2.36.0", tag="RELEASE_3_21")
	version("2.30.0", md5="8b3a3d5cd2698b4cef4396c388250658")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-matrix@1.2.6:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-ggplot2@1:", type=("build", "run"))
	depends_on("r-vgam@1.0.6:", type=("build", "run"))
	depends_on("r-ddrtree@0.1.4:", type=("build", "run"))
	depends_on("r-igraph@1.0.1:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-hsmmsinglecell@0.101.5:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-fastica", type=("build", "run"))
	depends_on("r-irlba@2:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-leidenbase@0.1.9:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-biocviews", type=("build", "run"))
	depends_on("r-rann@2.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-qlcmatrix", type=("build", "link", "run"))
