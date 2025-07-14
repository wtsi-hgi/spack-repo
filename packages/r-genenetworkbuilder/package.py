# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenenetworkbuilder(RPackage):
	"""GeneNetworkBuilder: a bioconductor package for building regulatory network using ChIP-chip/ChIP-seq data and Gene Expression Data

	Appliation for discovering direct or indirect targets of transcription factors using ChIP-chip or ChIP-seq, and microarray or RNA-seq gene expression data. Inputting a list of genes of potential targets of one TF from ChIP-chip or ChIP-seq, and the gene expression results, GeneNetworkBuilder generates a regulatory network of the TF.
	"""
	
	bioc = "GeneNetworkBuilder"

	version("1.50.0", commit="97920bfd6242d65a1c731ec80a3c9404b23bab04")
	version("1.44.0", commit="e57b56880705dc3fd6cca34ca3779caf80cf754b")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
