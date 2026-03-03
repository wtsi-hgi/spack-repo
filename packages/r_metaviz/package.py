# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetaviz(RPackage):
	"""Forest Plots, Funnel Plots, and Visual Funnel Plot Inference for
Meta-Analysis

	A compilation of functions to create visually appealing and information-rich 
    plots of meta-analytic data using 'ggplot2'. Currently allows to create forest plots, 
    funnel plots, and many of their variants, such as rainforest plots, thick forest plots, 
    additional evidence contour funnel plots, and sunset funnel plots. In addition, functionalities 
    for visual inference with the funnel plot in the context of meta-analysis are provided.
	"""
	
	homepage = "https://github.com/Mkossmeier/metaviz"
	cran = "metaviz" 

	version("0.3.1", md5="04d5c125b07b5d1b5961d5f251e63d58")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ggplot2@3.1:", type=("build", "run"))
	depends_on("r-nullabor@0.3.5:", type=("build", "run"))
	depends_on("r-dplyr@0.7.8:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r-metafor@1.9.9:", type=("build", "run"))
	depends_on("r-gridextra@2.2.1:", type=("build", "run"))
	depends_on("r-ggpubr@0.1.6:", type=("build", "run"))
