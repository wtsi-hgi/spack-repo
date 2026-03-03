# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBtllasso(RPackage):
	"""Modelling Heterogeneity in Paired Comparison Data

	Performs 'BTLLasso' as described by Schauberger and Tutz (2019) <doi:10.18637/jss.v088.i09> and Schauberger and Tutz (2017) <doi:10.1177/1471082X17693086>. BTLLasso is a method to include different types of variables in paired comparison models and, therefore, to allow for heterogeneity between subjects. Variables can be subject-specific, object-specific and subject-object-specific and can have an influence on the attractiveness/strength of the objects. Suitable L1 penalty terms are used to cluster certain effects and to reduce the complexity of the models.
	"""
	
	cran = "BTLLasso" 

	version("0.1-13", md5="62e1c1664b86e09d8dc152372efff948")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-psychotools", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
