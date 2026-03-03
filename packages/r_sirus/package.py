# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSirus(RPackage):
	"""Stable and Interpretable RUle Set

	A regression and classification algorithm based on random forests, which takes the form of a short list of rules. SIRUS combines the simplicity of decision trees with a predictivity close to random forests. The core aggregation principle of random forests is kept, but instead of aggregating predictions, SIRUS aggregates the forest structure: the most frequent nodes of the forest are selected to form a stable rule ensemble model. The algorithm is fully described in the following articles: Benard C., Biau G., da Veiga S., Scornet E. (2021), Electron. J. Statist., 15:427-505 <DOI:10.1214/20-EJS1792> for classification, and Benard C., Biau G., da Veiga S., Scornet E. (2021), AISTATS, PMLR 130:937-945 <http://proceedings.mlr.press/v130/benard21a>, for regression. This R package is a fork from the project ranger (<https://github.com/imbs-hl/ranger>). 
	"""
	
	homepage = "https://gitlab.com/drti/sirus"
	cran = "sirus" 

	version("0.3.3", md5="bef415a0abe9d7e5ead6b673537cb56b")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
