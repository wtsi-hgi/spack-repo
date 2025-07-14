# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDittoseq(RPackage):
	"""User Friendly Single-Cell and Bulk RNA Sequencing Visualization

	A universal, user friendly, single-cell and bulk RNA sequencing visualization toolkit that allows highly customizable creation of color blindness friendly, publication-quality figures. dittoSeq accepts both SingleCellExperiment (SCE) and Seurat objects, as well as the import and usage, via conversion to an SCE, of SummarizedExperiment or DGEList bulk data. Visualizations include dimensionality reduction plots, heatmaps, scatterplots, percent composition or expression across groups, and more. Customizations range from size and title adjustments to automatic generation of annotations for heatmaps, overlay of trajectory analysis onto any dimensionality reduciton plot, hidden data overlay upon cursor hovering via ggplotly conversion, and many more. All with simple, discrete inputs. Color blindness friendliness is powered by legend adjustments (enlarged keys), and by allowing the use of shapes or letter-overlay in addition to the carefully selected dittoColors().
	"""
	
	bioc = "dittoSeq"

	version("1.20.0", commit="6baca1cb7484351efb7930ea15bdc416a85a6873")
	version("1.14.3", commit="34da86479c9f5d8c60f193f088bc12bd0de2b7ff")
	version("1.14.2", md5="8cd8305d970fdd3e20c3db17aeb62502")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-colorspace@1.4:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
