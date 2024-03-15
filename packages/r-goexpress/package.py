# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGoexpress(RPackage):
	"""Visualise microarray and RNAseq data using gene ontology annotations

	The package contains methods to visualise the expression profile of genes from a microarray or RNA-seq experiment, and offers a supervised clustering approach to identify GO terms containing genes with expression levels that best classify two or more predefined groups of samples. Annotations for the genes present in the expression dataset may be obtained from Ensembl through the biomaRt package, if not provided by the user. The default random forest framework is used to evaluate the capacity of each gene to cluster samples according to the factor of interest. Finally, GO terms are scored by averaging the rank (alternatively, score) of their respective gene sets to cluster the samples. P-values may be computed to assess the significance of GO term ranking. Visualisation function include gene expression profile, gene ontology-based heatmaps, and hierarchical clustering of experimental samples using gene expression data.
	"""
	
	homepage = "https://github.com/kevinrue/GOexpress"
	bioc = "GOexpress" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GOexpress_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GOexpress/GOexpress_1.36.0.tar.gz"]

	version("1.36.0", md5="b313b2555495c3d3fc5674120b7bb01b")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-biobase@2.22:", type=("build", "run"))
	depends_on("r-biomart@2.18:", type=("build", "run"))
	depends_on("r-stringr@0.6.2:", type=("build", "run"))
	depends_on("r-ggplot2@0.9:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1:", type=("build", "run"))
	depends_on("r-gplots@2.13:", type=("build", "run"))
	depends_on("r-randomforest@4.6:", type=("build", "run"))
	depends_on("r-rcurl@1.95:", type=("build", "run"))
