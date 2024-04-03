# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBionero(RPackage):
	"""Biological Network Reconstruction Omnibus

	BioNERO aims to integrate all aspects of biological network inference in a single package, including data preprocessing, exploratory analyses, network inference, and analyses for biological interpretations. BioNERO can be used to infer gene coexpression networks (GCNs) and gene regulatory networks (GRNs) from gene expression data. Additionally, it can be used to explore topological properties of protein-protein interaction (PPI) networks. GCN inference relies on the popular WGCNA algorithm. GRN inference is based on the "wisdom of the crowds" principle, which consists in inferring GRNs with multiple algorithms (here, CLR, GENIE3 and ARACNE) and calculating the average rank for each interaction pair. As all steps of network analyses are included in this package, BioNERO makes users avoid having to learn the syntaxes of several packages and how to communicate between them. Finally, users can also identify consensus modules across independent expression sets and calculate intra and interspecies module preservation statistics between different networks.
	"""
	
	homepage = "https://github.com/almeidasilvaf/BioNERO"
	bioc = "BioNERO" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BioNERO_1.10.3.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BioNERO/BioNERO_1.10.3.tar.gz"]

	version("1.10.1", md5="cf8a0a4d5229ba0ff8060188e110f8f9")
	version("1.10.3", md5="207ef35f0131c41c1596683af729ed04")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-wgcna", type=("build", "run"))
	depends_on("r-dynamictreecut", type=("build", "run"))
	depends_on("r-ggdendro", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ggnetwork", type=("build", "run"))
	depends_on("r-intergraph", type=("build", "run"))
	depends_on("r-netrep", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-minet", type=("build", "run"))
	depends_on("r-genie3", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
