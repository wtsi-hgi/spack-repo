# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCetf(RPackage):
	"""Coexpression for Transcription Factors using Regulatory Impact Factors and Partial Correlation and Information Theory analysis

	This package provides the necessary functions for performing the Partial Correlation coefficient with Information Theory (PCIT) (Reverter and Chan 2008) and Regulatory Impact Factors (RIF) (Reverter et al. 2010) algorithm. The PCIT algorithm identifies meaningful correlations to define edges in a weighted network and can be applied to any correlation-based network including but not limited to gene co-expression networks, while the RIF algorithm identify critical Transcription Factors (TF) from gene expression data. These two algorithms when combined provide a very relevant layer of information for gene expression studies (Microarray, RNA-seq and single-cell RNA-seq data).
	"""
	
	bioc = "CeTF" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CeTF_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CeTF/CeTF_1.14.0.tar.gz"]

	version("1.20.0", tag="RELEASE_3_21")
	version("1.14.0", sha256="d250a6de29f0705dc4abee5987615c61173aa8508312c9e54c33b46379ab4087")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-clusterprofiler", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-genomictools-filehandler", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-ggnetwork", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcy3", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("curl", type=("build", "link", "run"))
	depends_on("libxml2", type=("build", "link", "run"))
	depends_on("openssl", type=("build", "link", "run"))
	depends_on("gcc", type=("build", "link", "run"))
	depends_on("zlib", type=("build", "link", "run"))
