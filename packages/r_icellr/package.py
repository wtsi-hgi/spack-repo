# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcellr(RPackage):
	"""Analyzing High-Throughput Single Cell Sequencing Data

	A toolkit that allows scientists to work with data from single cell sequencing technologies such as scRNA-seq, scVDJ-seq, scATAC-seq, CITE-Seq and Spatial Transcriptomics (ST). Single (i) Cell R package ('iCellR') provides unprecedented flexibility at every step of the analysis pipeline, including normalization, clustering, dimensionality reduction, imputation, visualization, and so on. Users can design both unsupervised and supervised models to best suit their research. In addition, the toolkit provides 2D and 3D interactive visualizations, differential expression analysis, filters based on cells, genes and clusters, data merging, normalizing for dropouts, data imputation methods, correcting for batch differences, pathway analysis, tools to find marker genes for clusters and conditions, predict cell types and pseudotime analysis. See Khodadadi-Jamayran, et al (2020) <doi:10.1101/2020.05.05.078550>  and Khodadadi-Jamayran, et al (2020) <doi:10.1101/2020.03.31.019109> for more details.
	"""
	
	homepage = "https://github.com/rezakj/iCellR"
	cran = "iCellR" 

	version("1.6.7", md5="11bf4c567e79f639c9d0fe4b9a39fe87")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-nbclust", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-ggdendro", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-uwot", type=("build", "run"))
	depends_on("r-hdf5r", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
