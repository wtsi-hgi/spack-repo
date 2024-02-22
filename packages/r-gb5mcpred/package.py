# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGb5mcpred(RPackage):
	"""Gradient Boosting Algorithm for Predicting Methylation States

	DNA methylation of 5-methylcytosine (5mC) is the result of a multi-step, enzyme-dependent process. Predicting these sites in-vitro is laborious, time consuming as well as costly. This ' Gb5mC-Pred ' package is an in-silico pipeline for predicting DNA sequences containing the 5mC sites. It uses a machine learning approach which uses Stochastic Gradient Boosting approach for prediction of the sequences with 5mC sites. This package has been developed by using the concept of Navarez and Roxas (2022) <doi:10.1109/TCBB.2021.3082184>.
	"""
	
	cran = "GB5mcPred" 

	version("0.1.0", md5="ac088d1e5b9e390fecd38579cd2a3774")

	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-splitstackshape", type=("build", "run"))
	depends_on("r-entropy", type=("build", "run"))
	depends_on("r-party", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ftrcool", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
