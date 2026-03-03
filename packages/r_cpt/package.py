# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCpt(RPackage):
	"""Classification Permutation Test

	Non-parametric test for equality of multivariate distributions.  Trains a classifier to classify (multivariate) observations as coming from one of several distributions.  If the classifier is able to classify the observations better than would be expected by chance (using permutation inference), then the null hypothesis that the distributions are equal is rejected.  
	"""
	
	homepage = "http://dept.stat.lsa.umich.edu/~johanngb"
	cran = "cpt" 

	version("1.0.2", md5="109f339cc8a64d957eeb40924fac6207")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
