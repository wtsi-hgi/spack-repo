# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RManhattanly(RPackage):
	"""Interactive Q-Q and Manhattan Plots Using 'plotly.js'

	Create interactive manhattan, Q-Q and volcano plots that are usable from the R console, 
    in 'Dash' apps, in the 'RStudio' viewer pane, in 'R Markdown' documents, and in 'Shiny' apps.
    Hover the mouse pointer over a point to show details or drag a rectangle to
    zoom. A manhattan plot is a popular graphical method for visualizing results
    from high-dimensional data analysis such as a (epi)genome wide association study
    (GWAS or EWAS), in which p-values, Z-scores, test statistics are plotted on a scatter
    plot against their genomic position. Manhattan plots are used for visualizing
    potential regions of interest in the genome that are associated with a phenotype.
    Interactive manhattan plots allow the inspection of specific value (e.g. rs number or
    gene name) by hovering the mouse over a cell, as well as zooming into a region of the
    genome (e.g. a chromosome) by dragging a rectangle around the relevant area.
    This work is based on the 'qqman' package and the 'plotly.js'
    engine. It produces similar manhattan and Q-Q plots as the 'manhattan' and 'qq'
    functions in the 'qqman' package, with the advantage of including extra annotation 
    information and interactive web-based visualizations directly from R. 
    Once uploaded to a 'plotly' account, 'plotly' graphs (and the data behind them) 
    can be viewed and modified in a web browser.
	"""
	
	homepage = "https://github.com/sahirbhatnagar/manhattanly/"
	cran = "manhattanly" 

	version("0.3.0", md5="76c53d4e541aebe68a4831b36bcbfec8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
