# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModelmap(RPackage):
	"""Modeling and Map Production using Random Forest and Related
Stochastic Models

	Creates sophisticated models of training data and validates the models with an independent test set, cross validation, or Out Of Bag (OOB) predictions on the training data. Create graphs and tables of the model validation results. Applies these models to GIS .img files of predictors to create detailed prediction surfaces. Handles large predictor files for map making, by reading in the .img files in chunks, and output to the .txt file the prediction for each data chunk, before reading the next chunk of data.
	"""
	
	cran = "ModelMap" 

	version("3.4.0.4", md5="667092dc267f603271f804b970a90f12")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-handtill2001", type=("build", "run"))
	depends_on("r-presenceabsence", type=("build", "run"))
