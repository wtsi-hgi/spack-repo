# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFactominer(RPackage):
	"""Multivariate Exploratory Data Analysis and Data Mining.

	Exploratory data analysis methods to summarize, visualize and describe
	datasets. The main principal component methods are available, those with
	the largest potential in terms of applications: principal component
	analysis (PCA) when variables are quantitative, correspondence analysis
	(CA) and multiple correspondence analysis (MCA) when variables are
	categorical, Multiple Factor Analysis when variables are structured in
	groups, etc. and hierarchical cluster analysis. F. Husson, S. Le and J.
	Pages (2017)."""

	cran = "FactoMineR"

	version("2.9", md5="63a4219b928ac66ecfd5cf5c302ff21c")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-emmeans", type=("build", "run"))
	depends_on("r-flashclust", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-leaps", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-multcompview", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
