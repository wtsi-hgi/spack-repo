# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatavisualizations(RPackage):
	"""Visualizations of High-Dimensional Data

	Gives access to data visualisation methods that are relevant from the data scientist's point of view. The flagship idea of 'DataVisualizations' is the mirrored density plot (MD-plot) for either classified or non-classified multivariate data published in Thrun, M.C. et al.: "Analyzing the Fine Structure of Distributions" (2020), PLoS ONE, <DOI:10.1371/journal.pone.0238835>. The MD-plot outperforms the box-and-whisker diagram (box plot), violin plot and bean plot and geom_violin plot of ggplot2. Furthermore, a collection of various visualization methods for univariate data is provided. In the case of exploratory data analysis, 'DataVisualizations' makes it possible to inspect the distribution of each feature of a dataset visually through a combination of four methods. One of these methods is the Pareto density estimation (PDE) of the probability density function (pdf). Additionally, visualizations of the distribution of distances using PDE, the scatter-density plot using PDE for two variables as well as the Shepard density plot and the Bland-Altman plot are presented here. Pertaining to classified high-dimensional data, a number of visualizations are described, such as f.ex. the heat map and silhouette plot. A political map of the world or Germany can be visualized with the additional information defined by a classification of countries or regions. By extending the political map further, an uncomplicated function for a Choropleth map can be used which is useful for measurements across a geographic area. For categorical features, the Pie charts, slope charts and fan plots, improved by the ABC analysis, become usable. More detailed explanations are found in the book by Thrun, M.C.: "Projection-Based Clustering through Self-Organization and Swarm Intelligence" (2018) <DOI:10.1007/978-3-658-20540-9>.
	"""
	
	homepage = "https://www.deepbionics.org/"
	cran = "DataVisualizations" 

	version("1.3.2", md5="bcebff0eaecdfb1dfbe8b393b2e621d2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
