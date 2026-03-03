# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegfilter(RPackage):
	"""Elimination of Noisy Samples in Regression Datasets using Noise
Filters

	Traditional noise filtering methods aim at removing noisy samples from a classification dataset. This package adapts classic and recent filtering techniques for use in regression problems, and it also incorporates methods specifically designed for regression data. In order to do this, it uses approaches proposed in the specialized literature, such as Martin et al. (2021) [<doi:10.1109/ACCESS.2021.3123151>] and Arnaiz-Gonzalez et al. (2016) [<doi:10.1016/j.eswa.2015.12.046>]. Thus, the goal of the implemented noise filters is to eliminate samples with noise in regression datasets.
	"""
	
	homepage = "https://github.com/juanmartinsantos/regfilter"
	cran = "regfilter" 

	version("1.1.1", md5="9fc43051d13b5ea4ab027b732cbbd21a")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-modelr", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-ubl", type=("build", "run"))
	depends_on("r-arules", type=("build", "run"))
	depends_on("r-infotheo", type=("build", "run"))
	depends_on("r-entropy", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
