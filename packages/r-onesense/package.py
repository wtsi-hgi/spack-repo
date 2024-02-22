# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROnesense(RPackage):
	"""One-Dimensional Soli-Expression by Nonlinear Stochastic Embedding (OneSENSE)

	A graphical user interface that facilitates the dimensional reduction method based on the t-distributed stochastic neighbor embedding (t-SNE) algorithm, for categorical analysis of mass cytometry data. With One-SENSE, measured parameters are grouped into predefined categories, and cells are projected onto a space composed of one dimension for each category. Each dimension is informative and can be annotated through the use of heatplots aligned in parallel to each axis, allowing for simultaneous visualization of two catergories across a two-dimensional plot. The cellular occupancy of the resulting plots alllows for direct assessment of the relationships between the categories.
	"""
	
	bioc = "oneSENSE" 

	version("1.24.0", commit="3f8955f2abfaf1c4333cb1d238c28353123e3b23")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-webshot", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyfiles", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
