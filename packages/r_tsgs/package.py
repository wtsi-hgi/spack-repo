# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsgs(RPackage):
	"""Trait Specific Gene Selection using SVM and GA

	Obtaining relevant set of trait specific genes from gene expression data is important for clinical diagnosis of disease and discovery of disease mechanisms in plants and animals. This process involves identification of relevant genes and removal of redundant genes as much as possible from a whole gene set. This package returns the trait specific gene set from the high dimensional RNA-seq count data by applying combination of two conventional machine learning algorithms, support vector machine (SVM) and genetic algorithm (GA). GA is used to control and optimize the subset of genes sent to the SVM for classification and evaluation. Genetic algorithm uses repeated learning steps and cross validation over number of possible solution and selects the best. The algorithm selects the set of genes based on a fitness function that is obtained via support vector machines. Using SVM as the classifier performance and the genetic algorithm for feature selection, a set of trait specific gene set is obtained.
	"""
	
	homepage = "https://github.com/SudhirSrivastava/TSGS"
	cran = "TSGS" 

	version("1.0", md5="bca3148d8e9ffd7025549799aa99583a")

	depends_on("r-caret", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-fastmatch", type=("build", "run"))
	depends_on("r-genalg", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
