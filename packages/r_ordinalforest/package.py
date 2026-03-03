# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrdinalforest(RPackage):
	"""Ordinal Forests: Prediction and Variable Ranking with Ordinal
Target Variables

	The ordinal forest (OF) method allows ordinal regression with high-dimensional
  and low-dimensional data. After having constructed an OF prediction rule using a training dataset, 
  it can be used to predict the values of the ordinal target variable for new observations.
  Moreover, by means of the (permutation-based) variable importance measure of OF, it is also
  possible to rank the covariates with respect to their importance in the prediction of the 
  values of the ordinal target variable.
  OF is presented in Hornung (2020).
  NOTE: Starting with package version 2.4, it is also possible to obtain class probability 
  predictions in addition to the class point predictions. Moreover, the variable importance values
  can also be based on the class probability predictions. Preliminary results indicate that
  this might lead to a better discrimination between influential and non-influential covariates.
  The main functions of the package are: ordfor() (construction of OF) and predict.ordfor() 
  (prediction of the target variable values of new observations).
  References:
  Hornung R. (2020) Ordinal Forests. Journal of Classification 37, 4–17. 
  <doi:10.1007/s00357-018-9302-x>.
	"""
	
	cran = "ordinalForest" 

	version("2.4-3", md5="a8d83163a2cdeb88e2f8a91f290ae953")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-verification", type=("build", "run"))
