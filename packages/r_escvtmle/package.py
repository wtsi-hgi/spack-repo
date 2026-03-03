# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REscvtmle(RPackage):
	"""Experiment-Selector CV-TMLE for Integration of Observational and
RCT Data

	The experiment selector cross-validated targeted maximum likelihood estimator (ES-CVTMLE) aims to select the experiment that optimizes the bias-variance tradeoff for estimating a causal average treatment effect (ATE) where different experiments may include a randomized controlled trial (RCT) alone or an RCT combined with real-world data. Using cross-validation, the ES-CVTMLE separates the selection of the optimal experiment from the estimation of the ATE for the chosen experiment. The estimated bias term in the selector is a function of the difference in conditional mean outcome under control for the RCT compared to the combined experiment. In order to help include truly unbiased external data in the analysis, the estimated average treatment effect on a negative control outcome may be added to the bias term in the selector. For more details about this method, please see Dang et al. (2022) <arXiv:2210.05802>.
	"""
	
	homepage = "https://github.com/Lauren-EylerDang/EScvtmle/tree/main"
	cran = "EScvtmle" 

	version("0.0.2", md5="603d00324a78128304f64347706b6712")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-superlearner@2.0.28:", type=("build", "run"))
	depends_on("r-origami@1.0.5:", type=("build", "run"))
	depends_on("r-dplyr@1.0.8:", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
	depends_on("r-mass@7.3.54:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.6:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
