# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMissforest(RPackage):
	"""Nonparametric Missing Value Imputation using Random Forest

	The function 'missForest' in this package is used to
        impute missing values particularly in the case of mixed-type
        data. It uses a random forest trained on the observed values of
        a data matrix to predict the missing values. It can be used to
        impute continuous and/or categorical data including complex
        interactions and non-linear relations. It yields an out-of-bag
        (OOB) imputation error estimate without the need of a test set
        or elaborate cross-validation. It can be run in parallel to 
        save computation time.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "missForest" 

	version("1.5", md5="cf0daa5e2b47df600f69a49840ed6f79")

	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-itertools", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
