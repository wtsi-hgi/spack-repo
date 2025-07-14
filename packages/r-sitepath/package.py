# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSitepath(RPackage):
	"""Phylogeny-based sequence clustering with site polymorphism

	Using site polymorphism is one of the ways to cluster DNA/protein sequences but it is possible for the sequences with the same polymorphism on a single site to be genetically distant. This package is aimed at clustering sequences using site polymorphism and their corresponding phylogenetic trees. By considering their location on the tree, only the structurally adjacent sequences will be clustered. However, the adjacent sequences may not necessarily have the same polymorphism. So a branch-and-bound like algorithm is used to minimize the entropy representing the purity of site polymorphism of each cluster.
	"""
	
	homepage = "https://wuaipinglab.github.io/sitePath/"
	bioc = "sitePath" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/sitePath_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/sitePath/sitePath_1.18.0.tar.gz"]

    version("1.24.0", tag="RELEASE_3_21")
	version("1.18.0", sha256="0436d1d9e105cfe74447db0c55a63e76ff1a47a4e49d1c89a5537b73d376b89d")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-aplot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-ggtree", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-tidytree", type=("build", "run"))
