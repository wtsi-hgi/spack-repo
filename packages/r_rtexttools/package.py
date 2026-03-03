# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtexttools(RPackage):
	"""Automatic Text Classification via Supervised Learning

	A machine learning package for automatic text classification 
	that makes it simple for novice users to get started with machine 
	learning, while allowing experienced users to easily experiment 
	with different settings and algorithm combinations. The package 
	includes eight algorithms for ensemble classification (svm, slda, 
	boosting, bagging, random forests, glmnet, decision trees, neural 
	networks), comprehensive analytics, and thorough documentation.
	"""
	
	homepage = "http://www.rtexttools.com/"
	cran = "RTextTools" 

	version("1.4.3", md5="6d4f1c9f91005cbc675c1a383e03cfec")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-sparsem", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-tree", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-ipred", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-tau", type=("build", "run"))
