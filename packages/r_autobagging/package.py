# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutobagging(RPackage):
	"""Learning to Rank Bagging Workflows with Metalearning

	A framework for automated machine learning. Concretely, the focus is on the optimisation of bagging workflows. A bagging workflows is composed by three phases: (i) generation: which and how many predictive models to learn; (ii) pruning: after learning a set of models, the worst ones are cut off from the ensemble; and (iii) integration: how the models are combined for predicting a new observation. autoBagging optimises these processes by combining metalearning and a learning to rank approach to learn from metadata. It automatically ranks 63 bagging workflows by exploiting past performance and dataset characterization. A complete description of the method can be found in: Pinto, F., Cerqueira, V., Soares, C., Mendes-Moreira, J. (2017): "autoBagging: Learning to Rank Bagging Workflows with Metalearning" arXiv preprint arXiv:1706.09367.
	"""
	
	cran = "autoBagging" 

	version("0.1.0", md5="c4bf3af43228cdf990e26b4de6deb0dd")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-entropy", type=("build", "run"))
	depends_on("r-lsr", type=("build", "run"))
	depends_on("r-corelearn", type=("build", "run"))
	depends_on("r-infotheo", type=("build", "run"))
	depends_on("r-minerva", type=("build", "run"))
	depends_on("r-party", type=("build", "run"))
