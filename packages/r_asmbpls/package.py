# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsmbpls(RPackage):
	"""Predicting and Classifying Patient Phenotypes with Multi-Omics
Data

	Adaptive Sparse Multi-block Partial Least Square, a supervised algorithm, is an extension of the Sparse Multi-block Partial Least Square, which allows different quantiles to be used in different blocks of different partial least square components to decide the proportion of features to be retained. The best combinations of quantiles can be chosen from a set of user-defined quantiles combinations by cross-validation. By doing this, it enables us to do the feature selection for different blocks, and the selected features can then be further used to predict the outcome. For example, in biomedical applications, clinical covariates plus different types of omics data such as microbiome, metabolome, mRNA data, methylation data, copy number variation data might be predictive for patients outcome such as survival time or response to therapy. Different types of data could be put in different blocks and along with survival time to fit the model. The fitted model can then be used to predict the survival for the new samples with the corresponding clinical covariates and omics data. In addition, Adaptive Sparse Multi-block Partial Least Square Discriminant Analysis is also included, which extends Adaptive Sparse Multi-block Partial Least Square for classifying the categorical outcome.
	"""
	
	cran = "asmbPLS" 

	version("1.0.0", md5="21133b6b07077d7f0c7231d0f3db5c46")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
