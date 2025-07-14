# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROutrider(RPackage):
	"""OUTRIDER - OUTlier in RNA-Seq fInDER

	Identification of aberrant gene expression in RNA-seq data. Read count expectations are modeled by an autoencoder to control for confounders in the data. Given these expectations, the RNA-seq read counts are assumed to follow a negative binomial distribution with a gene-specific dispersion. Outliers are then identified as read counts that significantly deviate from this distribution. Furthermore, OUTRIDER provides useful plotting functions to analyze and visualize the results.
	"""
	
	homepage = "https://github.com/gagneurlab/OUTRIDER"
	bioc = "OUTRIDER" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/OUTRIDER_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/OUTRIDER/OUTRIDER_1.20.0.tar.gz"]

    version("1.26.2", tag="RELEASE_3_21")
	version("1.20.0", sha256="cc932fd6bfa5007137d832ccd8ff5dc0be00cd420c34cec728c033adf0f43afb")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-bbmisc", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-deseq2@1.16.1:", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-heatmaply", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-pcamethods", type=("build", "run"))
	depends_on("r-prroc", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
