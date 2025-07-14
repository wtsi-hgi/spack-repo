# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REsetvis(RPackage):
	"""Visualizations of expressionSet Bioconductor object

	Utility functions for visualization of expressionSet (or SummarizedExperiment) Bioconductor object, including spectral map, tsne and linear discriminant analysis. Static plot via the ggplot2 package or interactive via the ggvis or rbokeh packages are available.
	"""
	
	bioc = "esetVis"

	version("1.34.0", commit="66c9cd7d446dca82da3621db0c801dea3fe79c3b")
	version("1.28.2", commit="35524e8a4ad5e39c32826bfb5a4b3d317d45d008")

	depends_on("r-mpm", type=("build", "run"))
	depends_on("r-hexbin", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-mlp", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
