# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIbst(RPackage):
	"""Improper Bagging Survival Tree

	Fit a full or subsampling bagging survival tree on a mixture of population (susceptible and nonsusceptible)
             using either a pseudo R2 criterion or an adjusted Logrank criterion. The predictor is 
             evaluated using the Out Of Bag Integrated Brier Score (IBS) and several scores of importance
             are computed for variable selection. The thresholds values for variable selection are 
             computed using a nonparametric permutation test. 
             See 'Cyprien Mbogning' and 'Philippe Broet' (2016)<doi:10.1186/s12859-016-1090-x> for 
             an overview about the methods implemented in this package.
	"""
	
	cran = "iBST" 

	version("1.2", md5="53a4914aa4c1ea99ea7b2990373020e5")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
