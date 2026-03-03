# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMissforestpredict(RPackage):
	"""Missing Value Imputation using Random Forest for Prediction
Settings

	Missing data imputation based on the 'missForest' algorithm (Stekhoven, Daniel J (2012) <doi:10.1093/bioinformatics/btr597>)
    with adaptations for prediction settings. The function missForest() is used 
    to impute a (training) dataset with missing values and to learn imputation 
    models that can be later used for imputing new observations. 
    The function missForestPredict() is used to impute one or multiple new 
    observations (test set) using the models learned on the training data. 
	"""
	
	homepage = "https://github.com/sibipx/missForestPredict"
	cran = "missForestPredict" 

	version("1.0", md5="c8a1d25edd34b7b9529ca865b4386b86")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
