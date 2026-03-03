# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlashlight(RPackage):
	"""Shed Light on Black Box Machine Learning Models

	Shed light on black box machine learning models by the help
    of model performance, variable importance, global surrogate models,
    ICE profiles, partial dependence (Friedman J. H. (2001)
    <doi:10.1214/aos/1013203451>), accumulated local effects (Apley D. W.
    (2016) <arXiv:1612.08468>), further effects plots, interaction
    strength, and variable contribution breakdown (Gosiewska and Biecek
    (2019) <arxiv:1903.11420>).  All tools are implemented to work with
    case weights and allow for stratified analysis.  Furthermore, multiple
    flashlights can be combined and analyzed together.
	"""
	
	homepage = "https://github.com/mayer79/flashlight"
	cran = "flashlight" 

	version("0.9.0", md5="398837712f57e1dadf4a3c30facd0dfa")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-metricsweighted@0.3:", type=("build", "run"))
	depends_on("r-rlang@0.3:", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-rpart-plot", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
