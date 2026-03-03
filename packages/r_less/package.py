# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLess(RPackage):
	"""Learning with Subset Stacking

	"Learning with Subset Stacking" is a supervised learning algorithm that is based on training many local estimators on subsets of a given dataset, and then passing their predictions to a global estimator. You can find the details about LESS in our manuscript at <arXiv:2112.06251>.
	"""
	
	cran = "less" 

	version("0.1.0", md5="457b60011194d26795e15627a49e70bb")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-mlmetrics", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-wordspace", type=("build", "run"))
