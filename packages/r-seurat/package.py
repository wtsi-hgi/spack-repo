# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeurat(RPackage):
	"""Tools for Single Cell Genomics.

	A toolkit for quality control, analysis, and exploration of single cell RNA
	sequencing data. 'Seurat' aims to enable users to identify and interpret
	sources of heterogeneity from single cell transcriptomic measurements, and
	to integrate diverse types of single cell data. See Satija R, Farrell J,
	Gennert D, et al (2015) <doi:10.1038/nbt.3192>, Macosko E, Basu A, Satija
	R, et al (2015) <doi:10.1016/j.cell.2015.05.002>, and Stuart T, Butler A,
	et al (2019) <doi:10.1016/j.cell.2019.05.031> for more details."""

	cran = "Seurat"

	version("4.4.0", md5="2cb0ba47a9d73bc8c985429fb316283e")

	depends_on("r@4.0.0:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-ggplot2@3.3.0:", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-ica", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-leiden@0.3.1:", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix@1.5-0:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-plotly@4.9.0:", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rcpp@1.0.7:", type=("build", "run"))
	depends_on("r-rcppannoy@0.0.18:", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-scattermore@1.2:", type=("build", "run"))
	depends_on("r-sctransform@0.4.0:", type=("build", "run"))
	depends_on("r-seuratobject@4.1.4:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-uwot@0.1.14:", type=("build", "run"))
	depends_on("r-rcpp@0.11.0:", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
