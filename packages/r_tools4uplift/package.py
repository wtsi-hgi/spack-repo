# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTools4uplift(RPackage):
	"""Tools for Uplift Modeling

	Uplift modeling aims at predicting the causal effect of an action such as a marketing campaign on a particular individual. In order to simplify the task for practitioners in uplift modeling, we propose a combination of tools that can be separated into the following ingredients: i) quantization, ii) visualization, iii) variable selection, iv) parameters estimation and, v) model validation. For more details, see <https://dms.umontreal.ca/~murua/research/UpliftRegression.pdf>.
	"""
	
	cran = "tools4uplift" 

	version("1.0.0", md5="b4789f17eae4bd1bd591212c685bf662")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-biasedurn", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-lhs", type=("build", "run"))
