# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKcsnbshiny(RPackage):
	"""Naive Bayes Classifier

	Predicts any variable in any categorical dataset for given values of predictor variables.
    If a dataset contains 4 variables, then any variable can be predicted based on the values of the other three variables given by the user. 
    The user can upload their own datasets and select what variable they want to predict.
    A 'handsontable' is provided to enter the predictor values and also accuracy of the prediction is also shown.
	"""
	
	homepage = "https://karnechaithanyasai.shinyapps.io/KCSNBShiny/"
	cran = "KCSNBShiny" 

	version("0.1.0", md5="4d7d401187415e7a2bba8190e41dec89")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rhandsontable", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
