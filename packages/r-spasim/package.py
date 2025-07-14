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

	version("1.10.0", commit="270e295d8b0526f5eef722e412c67c7235579d99")
	version("1.4.0", commit="185b59d3788d6230a3be8b290b78f1c09c2730a7")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-random", type=("build", "run"))
	depends_on("r-spatialexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
