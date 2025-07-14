# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBenchdamic(RPackage):
	"""Benchmark of differential abundance methods on microbiome data

	Starting from a microbiome dataset (16S or WMS with absolute count values) it is possible to perform several analysis to assess the performances of many differential abundance detection methods. A basic and standardized version of the main differential abundance analysis methods is supplied but the user can also add his method to the benchmark. The analyses focus on 4 main aspects: i) the goodness of fit of each method's distributional assumptions on the observed count data, ii) the ability to control the false discovery rate, iii) the within and between method concordances, iv) the truthfulness of the findings if any apriori knowledge is given. Several graphical functions are available for result visualization.
	"""
	
	bioc = "benchdamic" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/benchdamic_1.8.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/benchdamic/benchdamic_1.8.2.tar.gz"]

    version("1.14.2", tag="RELEASE_3_21")
	version("1.8.2", sha256="64656dce4654fdfad869e646da2fc59eca362b9c4e9a9f4bea32062bf548c50c")
	version("1.8.1", md5="ca158383ebf87138c91438c7946fe567")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-phyloseq", type=("build", "run"))
	depends_on("r-treesummarizedexperiment", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-zinbwave", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-aldex2", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-mast", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-ancombc", type=("build", "run"))
	depends_on("r-mixomics", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-noiseq", type=("build", "run"))
	depends_on("r-dearseq", type=("build", "run"))
	depends_on("r-microbiomestat", type=("build", "run"))
	depends_on("r-maaslin2", type=("build", "run"))
	depends_on("r-gunifrac", type=("build", "run"))
	depends_on("r-metagenomeseq", type=("build", "run"))
	depends_on("r-mglm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggdendro", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-tidytext", type=("build", "run"))
