# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHeatmaply(RPackage):
	"""Interactive Cluster Heat Maps Using 'plotly' and 'ggplot2'

	Create interactive cluster 'heatmaps' that can be saved as a stand-
    alone HTML file, embedded in 'R Markdown' documents or in a 'Shiny' app, and
    available in the 'RStudio' viewer pane. Hover the mouse pointer over a cell to
    show details or drag a rectangle to zoom. A 'heatmap' is a popular graphical
    method for visualizing high-dimensional data, in which a table of numbers
    are encoded as a grid of colored cells. The rows and columns of the matrix
    are ordered to highlight patterns and are often accompanied by 'dendrograms'.
    'Heatmaps' are used in many fields for visualizing observations, correlations,
    missing values patterns, and more. Interactive 'heatmaps' allow the inspection
    of specific value by hovering the mouse over a cell, as well as zooming into
    a region of the 'heatmap' by dragging a rectangle around the relevant area.
    This work is based on the 'ggplot2' and 'plotly.js' engine. It produces
    similar 'heatmaps' to 'heatmap.2' with the advantage of speed
    ('plotly.js' is able to handle larger size matrix), the ability to zoom from
    the 'dendrogram' panes, and the placing of factor variables in the sides of the
    'heatmap'.
	"""
	
	homepage = "https://talgalili.github.io/heatmaply/"
	cran = "heatmaply" 

	version("1.5.0", md5="c681c66008c0a446bc5c1c5083229996")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-plotly@4.7.1:", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-dendextend@1.12:", type=("build", "run"))
	depends_on("r-magrittr@1.0.1:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-seriation", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-webshot", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-egg", type=("build", "run"))
