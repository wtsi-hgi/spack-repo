# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNadia(RPackage):
	"""NA Data Imputation Algorithms

	Creates a uniform interface for several advanced imputations missing data methods. Every available method can be used as a part of 'mlr3' pipelines which allows easy tuning and performance evaluation. Most of the used functions work separately on the training and test sets (imputation is trained on the training set and impute training data. After that imputation is again trained on the test set and impute test data).
	"""
	
	cran = "NADIA" 

	version("0.4.2", md5="af04dd570be15406213897a82d4f5a57")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mlr3", type=("build", "run"))
	depends_on("r-mlr3pipelines", type=("build", "run"))
	depends_on("r-paradox", type=("build", "run"))
	depends_on("r-missforest", type=("build", "run"))
	depends_on("r-missmda", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-mlr3learners", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-amelia", type=("build", "run"))
	depends_on("r-vim", type=("build", "run"))
	depends_on("r-softimpute", type=("build", "run"))
	depends_on("r-missranger", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
