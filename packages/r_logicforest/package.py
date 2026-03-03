# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLogicforest(RPackage):
	"""Logic Forest

	Two classification ensemble methods based on logic regression models.  LogForest() uses a bagging approach to construct an ensemble of logic regression models.  LBoost() uses a combination of boosting and cross-validation to construct an ensemble of logic regression models.  Both methods are used for classification of binary responses based on binary predictors and for identification of important variables and variable interactions predictive of a binary outcome. Wolf, B.J., Slate, E.H., Hill, E.G. (2010) <doi:10.1093/bioinformatics/btq354>.
	"""
	
	cran = "LogicForest" 

	version("2.1.1", md5="e113513c659d2c77488051be1eff9bc4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-logicreg", type=("build", "run"))
