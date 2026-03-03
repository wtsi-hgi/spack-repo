# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutostepwiseglm(RPackage):
	"""Builds Stepwise GLMs via Train and Test Approach

	Randomly splits data into testing and training sets. Then, uses stepwise selection to fit numerous multiple regression models on the training data, and tests them on the test data. Returned for each model are plots comparing model Akaike Information Criterion (AIC), Pearson correlation coefficient (r) between the predicted and actual values, Mean Absolute Error (MAE), and R-Squared among the models. Each model is ranked relative to the other models by the model evaluation metrics (i.e., AIC, r, MAE, and R-Squared) and the model with the best mean ranking among the model evaluation metrics is returned. Model evaluation metric weights for AIC, r, MAE, and R-Squared are taken in as arguments as aic_wt, r_wt, mae_wt, and r_squ_wt, respectively. They are equally weighted as default but may be adjusted relative to each other if the user prefers one or more metrics to the others, Field, A. (2013, ISBN:978-1-4462-4918-5).
	"""
	
	cran = "AutoStepwiseGLM" 

	version("0.2.0", md5="6ad4a2b1722c5b293a1f8abebd1e991f")

	depends_on("r-caret", type=("build", "run"))
	depends_on("r-formula-tools", type=("build", "run"))
