# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMartini(RPackage):
	"""GWAS Incorporating Networks

	martini deals with the low power inherent to GWAS studies by using prior knowledge represented as a network. SNPs are the vertices of the network, and the edges represent biological relationships between them (genomic adjacency, belonging to the same gene, physical interaction between protein products). The network is scanned using SConES, which looks for groups of SNPs maximally associated with the phenotype, that form a close subnetwork.
	"""
	
	homepage = "https://github.com/hclimente/martini"
	bioc = "martini" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/martini_1.22.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/martini/martini_1.22.0.tar.gz"]

	version("1.22.0", md5="85e3366daf7ac24c0f50261fafe8b274")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-igraph@1.0.1:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-memoise@2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-snpstats@1.20:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.5:", type=("build", "run"))
