# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPomodoro(RPackage):
	"""Predictive Power of Linear and Tree Modeling

	Runs generalized and multinominal logistic (GLM and MLM) models, as well as random forest (RF), Bagging (BAG), and Boosting (BOOST). This package prints out to predictive outcomes easy for the selected data and data splits.
	"""
	
	homepage = "https://github.com/seymakalay/pomodoro"
	cran = "pomodoro" 

	version("3.8.0", md5="8c486bd80408eeb8e961f783d65032e8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-ipred", type=("build", "run"))
