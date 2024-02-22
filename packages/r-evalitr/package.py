# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvalitr(RPackage):
	"""Evaluating Individualized Treatment Rules

	Provides various statistical methods for evaluating
    Individualized Treatment Rules under randomized data. The provided
    metrics include Population Average Value (PAV), Population Average
    Prescription Effect (PAPE), Area Under Prescription Effect Curve
    (AUPEC). It also provides the tools to analyze Individualized
    Treatment Rules under budget constraints. Detailed reference in Imai
    and Li (2019) <arXiv:1905.05389>.
	"""
	
	homepage = "https://github.com/MichaelLLi/evalITR"
	cran = "evalITR" 

	version("1.0.0", md5="f47db9077dd5e0edf7905f0061fa762b")

	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-mass@7:", type=("build", "run"))
	depends_on("r-matrix@1:", type=("build", "run"))
	depends_on("r-quadprog@1:", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-ggdist", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-grf", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-rqpen", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-bartcause", type=("build", "run"))
	depends_on("r-superlearner", type=("build", "run"))
