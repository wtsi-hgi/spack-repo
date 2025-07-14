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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GeneNetworkBuilder_1.44.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GeneNetworkBuilder/GeneNetworkBuilder_1.44.0.tar.gz"]

    version("1.50.0", tag="RELEASE_3_21")
	version("1.44.0", sha256="1b7ce3b355694fdfcf4186e05bc245cd0c52fc5e572e56c754f66a5c6ca5e73f")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
