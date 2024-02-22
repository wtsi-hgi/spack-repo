# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlr3learners(RPackage):
	"""Recommended Learners for 'mlr3'

	Recommended Learners for 'mlr3'. Extends 'mlr3'
    with interfaces to essential machine learning packages on
    CRAN.  This includes, but is not limited to: (penalized) linear and
    logistic regression, linear and quadratic discriminant analysis,
    k-nearest neighbors, naive Bayes, support vector machines, and
    gradient boosting.
	"""
	
	homepage = "https://mlr3learners.mlr-org.com"
	cran = "mlr3learners" 

	version("0.5.8", md5="bd246c174bf2d937b9a7381e0c591f0a")

	depends_on("r-mlr3@0.14.1:", type=("build", "run"))
	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-mlr3misc@0.9.4:", type=("build", "run"))
	depends_on("r-paradox", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
