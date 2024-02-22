# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpot(RPackage):
	"""Sequential Parameter Optimization Toolbox

	A set of tools for model-based optimization and tuning of
    algorithms (hyperparameter tuning respectively hyperparameter optimization). It includes surrogate models, optimizers, and design of experiment
    approaches. The main interface is spot, which uses sequentially updated
    surrogate models for the purpose of efficient optimization. The main goal is
    to ease the burden of objective function evaluations, when a single evaluation
    requires a significant amount of resources.
	"""
	
	homepage = "https://www.spotseven.de"
	cran = "SPOT" 

	version("2.11.14", md5="2d69f52d5b003ebee8f1c2d55a96b733")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-deoptim", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-lagp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-plgp", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-rgenoud", type=("build", "run"))
	depends_on("r-rsm", type=("build", "run"))
