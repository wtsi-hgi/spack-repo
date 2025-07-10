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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/scDataviz_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/scDataviz/scDataviz_1.12.0.tar.gz"]

	version("1.12.0", sha256="47014950226c908536bac3ad2f9bd420a0b61d34221a7c394b9d2426579f15c1")

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
