# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRasclass(RPackage):
	"""Supervised Raster Image Classification

	Software to perform supervised and pixel based raster image classification. It has been designed to facilitate land-cover analysis. Five classification algorithms can be used: Maximum Likelihood Classification, Multinomial Logistic Regression, Neural Networks, Random Forests and Support Vector Machines. The output includes the classified raster and standard classification accuracy assessment such as the accuracy matrix, the overall accuracy and the kappa coefficient. An option for in-sample verification is available.
	"""
	
	cran = "rasclass" 

	version("0.2.2", md5="ae0e773d67590830619419e5c15d98a0")

	depends_on("r-car", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-rsnns", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
