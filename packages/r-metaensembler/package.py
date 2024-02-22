# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetaensembler(RPackage):
	"""Automated Intuitive Package for Meta-Ensemble Learning

	Extends the base classes and methods of 'caret' package for integration of base learners. The user can input the number of different base learners, and specify the final learner, along with the train-validation-test data partition split ratio. The predictions on the unseen new data is the resultant of the ensemble meta-learning <https://machinelearningmastery.com/stacking-ensemble-machine-learning-with-python/> of the heterogeneous learners aimed to reduce the generalization error in the predictive models. It significantly lowers the barrier for the practitioners to apply heterogeneous ensemble learning techniques in an amateur fashion to their everyday predictive problems. 
	"""
	
	cran = "metaEnsembleR" 

	version("0.1.0", md5="2ae7a36f8e83a5dfa34b887133069f6f")

	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
