# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCotan(RPackage):
	"""COexpression Tables ANalysis

	Statistical and computational method to analyze the co-expression of gene pairs at single cell level. It provides the foundation for single-cell gene interactome analysis. The basic idea is studying the zero UMI counts' distribution instead of focusing on positive counts; this is done with a generalized contingency tables framework. COTAN can effectively assess the correlated or anti-correlated expression of gene pairs. It provides a numerical index related to the correlation and an approximate p-value for the associated independence test. COTAN can also evaluate whether single genes are differentially expressed, scoring them with a newly defined global differentiation index. Moreover, this approach provides ways to plot and cluster genes according to their co-expression pattern with other genes, effectively helping the study of gene interactions and becoming a new tool to identify cell-identity marker genes.
	"""
	
	homepage = "https://github.com/seriph78/COTAN"
	bioc = "COTAN" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/COTAN_2.2.3.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/COTAN/COTAN_2.2.3.tar.gz"]

	version("2.2.3", md5="a3d6f259a1ad5ac8203558ca7e61a91b")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-parallelly", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-biocsingular", type=("build", "run"))
	depends_on("r-pcatools", type=("build", "run"))
	depends_on("r-paralleldist", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-umap", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-zeallot", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
