# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBionar(RPackage):
	"""Biological Network Analysis in R

	the R package BioNAR, developed to step by step analysis of PPI network. The aim is to quantify and rank each protein’s simultaneous impact into multiple complexes based on network topology and clustering. Package also enables estimating of co-occurrence of diseases across the network and specific clusters pointing towards shared/common mechanisms.
	"""
	
	bioc = "BioNAR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BioNAR_1.4.4.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BioNAR/BioNAR_1.4.4.tar.gz"]

	version("1.10.0", tag="RELEASE_3_21")
	version("1.4.4", sha256="4dfa5a4cfe10b5dd63b7a63b6be43c6ae87cbb2098e5165d3ec7e92d6979dabe")
	version("1.4.1", md5="cce2273d564095b70d5b18aa6d134612")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-igraph@2.0.1.1:", type=("build", "run"))
	depends_on("r-powerlaw", type=("build", "run"))
	depends_on("r-latex2exp", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-clustercons", type=("build", "run"))
	depends_on("r-fgsea", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-rspectral", type=("build", "run"))
	depends_on("r-wgcna", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
