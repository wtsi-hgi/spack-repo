# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhemd(RPackage):
	"""Phenotypic EMD for comparison of single-cell samples

	Package for comparing and generating a low-dimensional embedding of multiple single-cell samples.
	"""
	
	bioc = "phemd" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/phemd_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/phemd/phemd_1.18.0.tar.gz"]

	version("1.18.0", sha256="03c5354299deefdf02142f4fc7d8464aac1489a62b719f1caf026b1b8db8929c")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-monocle", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-transport", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-destiny", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-maptree", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-phater", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
