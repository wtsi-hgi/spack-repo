# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *


class RGoplot(RPackage):
	"""Visualization of Functional Analysis Data.

	Implementation of multilayered visualizations for enhanced graphical
	representation of functional analysis data. It combines and integrates
	omics data derived from expression and functional annotation enrichment
	analyses. Its plotting functions have been developed with an hierarchical
	structure in mind: starting from a general overview to identify the most
	enriched categories (modified bar plot, bubble plot) to a more detailed one
	displaying different types of relevant information for the molecules in a
	given set of categories (circle plot, chord plot, cluster plot, Venn
	diagram, heatmap)."""

	cran = "GOplot"

	version("1.0.2", md5="e06a7705b6564c82dc01c5e0a3c91984")

	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-ggdendro@0.1.17:", type=("build", "run"))
	depends_on("r-gridextra@2:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r@3.2.3:", type=("build", "run"))
