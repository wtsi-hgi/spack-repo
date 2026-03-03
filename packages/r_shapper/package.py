# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShapper(RPackage):
	"""Wrapper of Python Library 'shap'

	Provides SHAP explanations of machine learning models. In applied machine learning, there is a strong belief that we need to strike a balance between interpretability and accuracy. However, in field of the Interpretable Machine Learning, there are more and more new ideas for explaining black-box models. One of the best known method for local explanations is SHapley Additive exPlanations (SHAP) introduced by Lundberg, S., et al., (2016) <arXiv:1705.07874> The SHAP method is used to calculate influences of variables on the particular observation. This method is based on Shapley values, a technique used in game theory. The R package 'shapper' is a port of the Python library 'shap'. 
	"""
	
	homepage = "https://github.com/ModelOriented/shapper"
	cran = "shapper" 

	version("0.1.3", md5="ba5831e83076133527a1118a3940c68d")

	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-dalex", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
