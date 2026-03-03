# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRadiantModel(RPackage):
	"""Model Menu for Radiant: Business Analytics using R and Shiny

	The Radiant Model menu includes interfaces for linear and logistic
    regression, naive Bayes, neural networks, classification and regression trees,
    model evaluation, collaborative filtering, decision analysis, and simulation. 
    The application extends the functionality in 'radiant.data'.
	"""
	
	homepage = "https://github.com/radiant-rstats/radiant.model/"
	cran = "radiant.model" 

	version("1.6.3", md5="fe225a41278c3d068f1673669330f16e")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-radiant-data@1.5.3:", type=("build", "run"))
	depends_on("r-radiant-basics@1.5:", type=("build", "run"))
	depends_on("r-shiny@1.7.4:", type=("build", "run"))
	depends_on("r-nnet@7.3.12:", type=("build", "run"))
	depends_on("r-neuralnettools@1.5.1:", type=("build", "run"))
	depends_on("r-sandwich@2.3.4:", type=("build", "run"))
	depends_on("r-car@2.1.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.4.2:", type=("build", "run"))
	depends_on("r-scales@1.2.1:", type=("build", "run"))
	depends_on("r-data-tree@0.7.4:", type=("build", "run"))
	depends_on("r-stringr@1.1:", type=("build", "run"))
	depends_on("r-lubridate@1.7.2:", type=("build", "run"))
	depends_on("r-tidyr@0.8.2:", type=("build", "run"))
	depends_on("r-dplyr@1.1.2:", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
	depends_on("r-rlang@0.4.10:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-diagrammer@1.0.9:", type=("build", "run"))
	depends_on("r-import@1.1:", type=("build", "run"))
	depends_on("r-psych@1.8.4:", type=("build", "run"))
	depends_on("r-e1071@1.6.8:", type=("build", "run"))
	depends_on("r-rpart@4.1.11:", type=("build", "run"))
	depends_on("r-ggrepel@0.8:", type=("build", "run"))
	depends_on("r-broom@0.7:", type=("build", "run"))
	depends_on("r-patchwork@1:", type=("build", "run"))
	depends_on("r-ranger@0.11.2:", type=("build", "run"))
	depends_on("r-xgboost@1.6.0.1:", type=("build", "run"))
	depends_on("r-pdp@0.8.1:", type=("build", "run"))
	depends_on("r-vip@0.3.2:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
