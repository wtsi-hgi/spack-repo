# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMice(RPackage):
	"""Multivariate Imputation by Chained Equations.

	Multiple imputation using Fully Conditional Specification (FCS) implemented
	by the MICE algorithm as described in Van Buuren and Groothuis-Oudshoorn
	(2011) <doi:10.18637/jss.v045.i03>.  Each variable has its own imputation
	model. Built-in imputation models are provided for continuous data
	(predictive mean matching, normal), binary data (logistic regression),
	unordered categorical data (polytomous logistic regression) and ordered
	categorical data (proportional odds). MICE can also impute continuous
	two-level data (normal model, pan, second-level variables). Passive
	imputation can be used to maintain consistency between variables. Various
	diagnostic plots are available to inspect the quality of the
	imputations."""

	cran = "mice"

	license("GPL-2.0-or-later")

	version("3.16.0", md5="0e44a4e8e2f690d7393e90568b5b6e08")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-mitml", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
