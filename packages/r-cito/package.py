# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCito(RPackage):
	"""Building and Training Neural Networks

	The 'cito' package provides a user-friendly interface for training and interpreting deep neural networks (DNN). 'cito' simplifies the fitting of DNNs by supporting the familiar formula syntax, hyperparameter tuning under cross-validation, and helps to detect and handle convergence problems.  DNNs can be trained on CPU, GPU and MacOS GPUs. In addition, 'cito' has many downstream functionalities such as various explainable AI (xAI) metrics (e.g. variable importance, partial dependence plots, accumulated local effect plots, and effect estimates) to interpret trained DNNs. 'cito' optionally provides confidence intervals (and p-values) for all xAI metrics and predictions. At the same time, 'cito' is computationally efficient because it is based on the deep learning framework 'torch'. The 'torch' package is native to R, so no Python installation or other API is required for this package.
	"""
	
	homepage = "https://citoverse.github.io/cito/"
	cran = "cito" 

	version("1.0.2", md5="7b48f67506c33fe27fe75ee09d2f9fcd")
	version("1.1", md5="f672d8eca063d2adb88d36f1a8e211b1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-coro", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-torch", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-parabar", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-torchvision", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
