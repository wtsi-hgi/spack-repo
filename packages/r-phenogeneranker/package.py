# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhenogeneranker(RPackage):
	"""PhenoGeneRanker: A gene and phenotype prioritization tool

	This package is a gene/phenotype prioritization tool that utilizes multiplex heterogeneous gene phenotype network. PhenoGeneRanker allows multi-layer gene and phenotype networks. It also calculates empirical p-values of gene/phenotype ranking using random stratified sampling of genes/phenotypes based on their connectivity degree in the network. https://dl.acm.org/doi/10.1145/3307339.3342155.
	"""
	
	bioc = "PhenoGeneRanker" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/PhenoGeneRanker_1.10.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/PhenoGeneRanker/PhenoGeneRanker_1.10.0.tar.gz"]

	version("1.10.0", md5="a6530ed180fae6b4250bc56d3de24e19")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
