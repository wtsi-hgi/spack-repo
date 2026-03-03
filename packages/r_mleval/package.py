# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMleval(RPackage):
	"""Machine Learning Model Evaluation

	Straightforward and detailed evaluation of machine learning models. 'MLeval' can produce receiver operating characteristic (ROC) curves, precision-recall (PR) curves, calibration curves, and PR gain curves. 'MLeval' accepts a data frame of class probabilities and ground truth labels, or, it can automatically interpret the Caret train function results from repeated cross validation, then select the best model and analyse the results. 'MLeval' produces a range of evaluation metrics with confidence intervals.
	"""
	
	cran = "MLeval" 

	version("0.3", md5="68472e0d1bf17769ef47fd9735698f38")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
