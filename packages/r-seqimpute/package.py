# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqimpute(RPackage):
	"""Imputation of Missing Data in Sequence Analysis

	Multiple imputation of missing data present in a dataset through the prediction based on either a random forest or a multinomial regression model. Covariates and time-dependant covariates can be included in the model. The prediction of the missing values is based on the method of Halpin (2012) <https://researchrepository.ul.ie/articles/report/Multiple_imputation_for_life-course_sequence_data/19839736>.
	"""
	
	cran = "seqimpute" 

	version("1.8", md5="189cae316c987c65a662233549750a87")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-amelia", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-traminer", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-swfscmisc", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dfidx", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-mlr", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
