# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowml(RPackage):
	"""A Backend for a 'nextflow' Pipeline that Performs
Machine-Learning-Based Modeling of Biomedical Data

	Provides functionality to perform machine-learning-based modeling in a computation pipeline.
    Its functions contain the basic steps of machine-learning-based knowledge discovery workflows,
    including model training and optimization, model evaluation, and model testing.
    To perform these tasks, the package builds heavily on existing machine-learning packages,
    such as 'caret' <https://github.com/topepo/caret/> and associated packages.
    The package can train multiple models, optimize model hyperparameters by performing a grid search
    or a random search, and evaluates model performance by different metrics.
    Models can be validated either on a test data set, or in case of a small sample size
    by k-fold cross validation or repeated bootstrapping.
    It also allows for 0-Hypotheses generation by performing permutation experiments.
    Additionally, it offers methods of model interpretation and item categorization
    to identify the most informative features from a high dimensional data space.
    The functions of this package can easily be integrated into computation pipelines
    (e.g. 'nextflow' <https://www.nextflow.io/>) and hereby improve scalability,
    standardization, and re-producibility in the context of machine-learning.
	"""
	
	homepage = "https://github.com/Boehringer-Ingelheim/flowml"
	cran = "flowml" 

	version("0.1.3", md5="20dc467fadd3e6834589de779b361bd0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-abcanalysis", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fastshap", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-optparse", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rsample", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-vip", type=("build", "run"))
