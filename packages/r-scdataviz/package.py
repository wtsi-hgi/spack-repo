# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScdataviz(RPackage):
	"""scDataviz: single cell dataviz and downstream analyses

	In the single cell World, which includes flow cytometry, mass cytometry, single-cell RNA-seq (scRNA-seq), and others, there is a need to improve data visualisation and to bring analysis capabilities to researchers even from non-technical backgrounds. scDataviz attempts to fit into this space, while also catering for advanced users. Additonally, due to the way that scDataviz is designed, which is based on SingleCellExperiment, it has a 'plug and play' feel, and immediately lends itself as flexibile and compatibile with studies that go beyond scDataviz. Finally, the graphics in scDataviz are generated via the ggplot engine, which means that users can 'add on' features to these with ease.
	"""
	
	homepage = "https://github.com/kevinblighe/scDataviz"
	bioc = "scDataviz"

	version("1.18.0", commit="3e7aa1bb4d5e4c238645f15e45621ca3c4e69973")
	version("1.12.0", commit="669e4634363311fb7214e3adebaadc0194a8295b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-umap", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
