# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIngredients(RPackage):
	"""Effects and Importances of Model Ingredients

	Collection of tools for assessment of feature importance and feature effects.
    Key functions are:
    feature_importance() for assessment of global level feature importance,
    ceteris_paribus() for calculation of the what-if plots,
    partial_dependence() for partial dependence plots,
    conditional_dependence() for conditional dependence plots,
    accumulated_dependence() for accumulated local effects plots,
    aggregate_profiles() and cluster_profiles() for aggregation of ceteris paribus profiles,
    generic print() and plot() for better usability of selected explainers,
    generic plotD3() for interactive, D3 based explanations, and
    generic describe() for explanations in natural language.
    The package 'ingredients' is a part of the 'DrWhy.AI' universe (Biecek 2018) <arXiv:1806.08915>.
	"""
	
	homepage = "https://ModelOriented.github.io/ingredients/"
	cran = "ingredients" 

	version("2.3.0", md5="46458d9e09b13c884e88f8ebfdcd5a29")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
