# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMachineshop(RPackage):
	"""Machine Learning Models and Tools

	Meta-package for statistical and machine learning with a unified
    interface for model fitting, prediction, performance assessment, and
    presentation of results.  Approaches for model fitting and prediction of
    numerical, categorical, or censored time-to-event outcomes include
    traditional regression models, regularization methods, tree-based methods,
    support vector machines, neural networks, ensembles, data preprocessing,
    filtering, and model tuning and selection.  Performance metrics are provided
    for model assessment and can be estimated with independent test sets, split
    sampling, cross-validation, or bootstrap resampling.  Resample estimation
    can be executed in parallel for faster processing and nested in cases of
    model tuning and selection.  Modeling results can be summarized with
    descriptive statistics; calibration curves; variable importance; partial
    dependence plots; confusion matrices; and ROC, lift, and other performance
    curves.
	"""
	
	homepage = "https://brian-j-smith.github.io/MachineShop/"
	cran = "MachineShop" 

	version("3.7.0", md5="7d8cf20f8cefd4fe374282890788ce54")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-cli@3.1:", type=("build", "run"))
	depends_on("r-dials@0.0.4:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix@1.5.0:", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-party", type=("build", "run"))
	depends_on("r-polspline", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-recipes@1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rsample@1.1:", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
