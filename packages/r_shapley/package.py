# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShapley(RPackage):
	"""Weighted Mean SHAP for Feature Selection in ML Grid and Ensemble

	This R package introduces an innovative method for calculating SHapley Additive exPlanations (SHAP) values 
             for a grid of fine-tuned base-learner machine learning models as well as stacked ensembles, a method not 
             previously available due to the common reliance on single best-performing models. By integrating the weighted 
             mean SHAP values from individual base-learners comprising the ensemble or individual base-learners in a tuning grid search, 
             the package weights SHAP contributions according to each model's performance, assessed by the Area Under the 
             Precision-Recall Curve (AUCPR) for binary classifiers (currently implemented). It further extends this framework to 
             implement weighted confidence intervals for weighted mean SHAP values, offering a more comprehensive and robust 
             feature importance evaluation over a grid of machine learning models, instead of solely computing SHAP values for 
             the best-performing model. This methodology is particularly beneficial for addressing the severe class imbalance 
             (class rarity) problem by providing a transparent, generalized measure of feature importance that mitigates the 
             risk of reporting SHAP values for an overfitted or biased model and maintains robustness under severe class imbalance,
             where there is no universal criteria of identifying the absolute best model. Furthermore, the package implements
             hypothesis testing to ascertain the statistical significance of SHAP values for individual features, as well as 
             comparative significance testing of SHAP contributions between features. Additionally, it tackles a critical 
             gap in feature selection literature by presenting criteria for the automatic feature selection of the most important 
             features across a grid of models or stacked ensembles, eliminating the need for arbitrary determination of the 
             number of top features to be extracted. This utility is invaluable for researchers analyzing feature significance, 
             particularly within severely imbalanced outcomes where conventional methods fall short. In addition, it is also 
             expected to report democratic feature importance across a grid of models, resulting in a more comprehensive and 
             generalizable feature selection. The package further implements a novel method for visualizing SHAP values both 
             at subject level and feature level as well as a plot for feature selection based on the weighted mean SHAP ratios.
	"""
	
	homepage = "https://github.com/haghish/shapley"
	cran = "shapley" 

	version("0.1", md5="c59a37417415817191e9a89029856a69")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.4.2:", type=("build", "run"))
	depends_on("r-h2o@3.34:", type=("build", "run"))
	depends_on("r-curl@4.3:", type=("build", "run"))
	depends_on("r-waffle@1.0.2:", type=("build", "run"))
