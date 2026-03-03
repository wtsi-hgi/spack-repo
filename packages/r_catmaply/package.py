# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCatmaply(RPackage):
	"""Heatmap for Categorical Data using 'plotly'

	Methods and plotting functions for displaying categorical data on an 
             interactive heatmap using 'plotly'. Provides functionality for strictly 
             categorical heatmaps, heatmaps illustrating categorized continuous data 
             and annotated heatmaps. Also, there are various options to interact with the x-axis
             to prevent overlapping axis labels, e.g. via simple sliders or range sliders. 
             Besides the viewer pane, resulting plots can be saved as a standalone HTML file, 
             embedded in 'R Markdown' documents or in a 'Shiny' app.
	"""
	
	homepage = "https://github.com/VerkehrsbetriebeZuerich/catmaply"
	cran = "catmaply" 

	version("0.9.4", md5="3d4fa413157e215750339d53ffcefd47")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
