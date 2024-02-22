# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmdh2(RPackage):
	"""Binary Classification via GMDH-Type Neural Network Algorithms

	Performs binary classification via Group Method of Data Handling (GMDH) - type neural network algorithms. There exist two main algorithms available in GMDH() and dceGMDH() functions. GMDH() performs classification via GMDH algorithm for a binary response and returns important variables. dceGMDH() performs classification via diverse classifiers ensemble based on GMDH (dce-GMDH) algorithm. Also, the package produces a well-formatted table of descriptives for a binary response. Moreover, it produces confusion matrix, its related statistics and scatter plot (2D and 3D) with classification labels of binary classes to assess the prediction performance. All 'GMDH2' functions are designed for a binary response (Dag et al., 2019, <https://download.atlantis-press.com/article/125911202.pdf>).
	"""
	
	homepage = "http://www.softmed.hacettepe.edu.tr/GMDH2"
	cran = "GMDH2" 

	version("1.8", md5="6b3a68c80dcd94165d9c6594dcd4e3f8", url="https://cran.r-project.org/src/contrib/GMDH2_1.8.tar.gz")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
