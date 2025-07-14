# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCytomapper(RPackage):
	"""Visualization of highly multiplexed imaging data in R

	Highly multiplexed imaging acquires the single-cell expression of selected proteins in a spatially-resolved fashion. These measurements can be visualised across multiple length-scales. First, pixel-level intensities represent the spatial distributions of feature expression with highest resolution. Second, after segmentation, expression values or cell-level metadata (e.g. cell-type information) can be visualised on segmented cell areas. This package contains functions for the visualisation of multiplexed read-outs and cell-level information obtained by multiplexed imaging technologies. The main functions of this package allow 1. the visualisation of pixel-level information across multiple channels, 2. the display of cell-level information (expression and/or metadata) on segmentation masks and 3. gating and visualisation of single cells.
	"""
	
	homepage = "https://github.com/BodenmillerGroup/cytomapper"
	bioc = "cytomapper" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/cytomapper_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/cytomapper/cytomapper_1.14.0.tar.gz"]

    version("1.20.0", tag="RELEASE_3_21")
	version("1.14.0", sha256="e95ea205532162727bf4a3e54bdc0a7d7978966d0364fe33f46875e8a1e4e13b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ebimage", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-spatialexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-hdf5array", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggbeeswarm", type=("build", "run"))
	depends_on("r-svgpanzoom", type=("build", "run"))
	depends_on("r-svglite", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-nnls", type=("build", "run"))
