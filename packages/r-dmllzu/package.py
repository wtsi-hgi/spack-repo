# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDmllzu(RPackage):
	"""Double Machine Learning

	Yang(2020,<doi:10.1016/j.jeconom.2020.01.018>) come up with Double Machine Learning model ,it is based on this model, using four machine learning methods-- bagging, Boosting, random forest and neural network, and then  based on the four models   for two different combinations of the integrated model -- linear model combination and random forest .  
	"""
	
	cran = "DMLLZU" 

	version("0.1.1", md5="a1fa88d66378d7e210d008a29b65f5d3")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-islr", type=("build", "run"))
