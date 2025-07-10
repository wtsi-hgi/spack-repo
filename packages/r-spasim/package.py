# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpasim(RPackage):
	"""Spatial point data simulator for tissue images

	A suite of functions for simulating spatial patterns of cells in tissue images. Output images are multitype point data in SingleCellExperiment format. Each point represents a cell, with its 2D locations and cell type. Potential cell patterns include background cells, tumour/immune cell clusters, immune rings, and blood/lymphatic vessels.
	"""
	
	homepage = "https://trigosteam.github.io/spaSim/"
	bioc = "spaSim" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/spaSim_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/spaSim/spaSim_1.4.0.tar.gz"]

	version("1.4.0", sha256="73fd96426fae25af657f6585746132fcf83798b59c8fd9ff620d9b852ace4638")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-random", type=("build", "run"))
	depends_on("r-spatialexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
