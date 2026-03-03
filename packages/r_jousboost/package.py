# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJousboost(RPackage):
	"""Implements Under/Oversampling for Probability Estimation

	Implements under/oversampling for probability estimation.  To be
    used with machine learning methods such as AdaBoost, random forests, etc.
	"""
	
	cran = "JOUSBoost" 

	version("2.1.0", md5="3dcfd66f6126eee907cb76e01127e4c2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
