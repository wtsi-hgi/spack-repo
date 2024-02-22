# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemiartificial(RPackage):
	"""Generator of Semi-Artificial Data

	Contains methods to generate and evaluate semi-artificial data sets. 
 Based on a given data set different methods learn data properties using machine learning algorithms and
 generate new data with the same properties.
 The package currently includes the following data generators:
  i) a RBF network based generator using rbfDDA() from package 'RSNNS',
  ii) a Random Forest based generator for both classification and regression problems
  iii) a density forest based generator for unsupervised data
 Data evaluation support tools include:
  a) single attribute based statistical evaluation: mean, median, standard deviation, skewness, kurtosis, medcouple, L/RMC, KS test, Hellinger distance
  b) evaluation based on clustering using Adjusted Rand Index (ARI) and FM
  c) evaluation based on classification performance with various learning models, e.g., random forests.
	"""
	
	homepage = "http://lkm.fri.uni-lj.si/rmarko/software/"
	cran = "semiArtificial" 

	version("2.4.1", md5="f3c06fe64fd1984c13b46953569e105a")

	depends_on("r-corelearn@1.50.3:", type=("build", "run"))
	depends_on("r-rsnns", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-fpc", type=("build", "run"))
	depends_on("r-timedate", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-logspline", type=("build", "run"))
	depends_on("r-mcclust", type=("build", "run"))
	depends_on("r-flexclust", type=("build", "run"))
	depends_on("r-statmatch", type=("build", "run"))
