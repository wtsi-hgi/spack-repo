# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScider(RPackage):
	"""Spatial cell-type inter-correlation by density in R

	scider is an user-friendly R package providing functions to model the global density of cells in a slide of spatial transcriptomics data. All functions in the package are built based on the SpatialExperiment object, allowing integration into various spatial transcriptomics-related packages from Bioconductor. After modelling density, the package allows for serveral downstream analysis, including colocalization analysis, boundary detection analysis and differential density analysis.
	"""
	
	homepage = "https://github.com/ChenLaboratory/scider"
	bioc = "scider" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/scider_1.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/scider/scider_1.0.0.tar.gz"]

    version("1.6.0", tag="RELEASE_3_21")
	version("1.0.0", sha256="0b54660caa2f18fa624319f51f8971d29e067b56546f4bfd50cfb4dd5f8187e6")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-spatialexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-lwgeom", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-isoband", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
