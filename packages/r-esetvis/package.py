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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/esetVis_1.28.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/esetVis/esetVis_1.28.2.tar.gz"]

	version("1.28.2", sha256="74a834d41fe5171446f6d231f14d6b1c276e4c3b9cbf485e20349b02f0f860f9")

	depends_on("r-mpm", type=("build", "run"))
	depends_on("r-hexbin", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-mlp", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
