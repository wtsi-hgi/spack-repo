# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKcsknnshiny(RPackage):
	"""K-Nearest Neighbour Classifier

	It predicts any attribute (categorical) given a set of input numeric predictor values. Note that only numeric input predictors should be given.
             The k value can be chosen according to accuracies provided. The attribute to be predicted can be selected from the dropdown provided (select categorical attribute).
             This is because categorical attributes cannot be given as inputs here. A 'handsontable' is also provided to enter the input predictor values.
	"""
	
	cran = "KCSKNNShiny" 

	version("0.1.0", md5="21fc932c7b9b9cd0980a39573a154950")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rhandsontable", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
