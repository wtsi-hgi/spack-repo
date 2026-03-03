# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCitrus(RPackage):
	"""Customer Intelligence Tool for Rapid Understandable Segmentation

	A tool to easily run and visualise supervised and unsupervised state of the art customer segmentation. 
    It is built like a pipeline covering the 3 main steps in a segmentation project: pre-processing, modelling, and plotting.
    Users can either run the pipeline as a whole, or choose to run any one of the three individual steps.
    It is equipped with a supervised option (tree optimisation) and an unsupervised option (k-clustering) as default models.
	"""
	
	cran = "citrus" 

	version("1.0.2", md5="fb75d53115e168aff323846ee0c27986")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-ggally@2:", type=("build", "run"))
	depends_on("r-clustmixtype@0.1.16:", type=("build", "run"))
	depends_on("r-treeclust@1.1.7:", type=("build", "run"))
	depends_on("r-rpart@4.1.15:", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-rpart-plot@3.0.7:", type=("build", "run"))
	depends_on("r-stringr@1.3:", type=("build", "run"))
	depends_on("r-dplyr@1.0.6:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r-rlang@0.4.9:", type=("build", "run"))
