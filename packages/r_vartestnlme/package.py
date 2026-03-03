# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVartestnlme(RPackage):
	"""Variance Components Testing for Linear and Nonlinear Mixed
Effects Models

	An implementation of the Likelihood ratio Test (LRT) for testing that,
    in a (non)linear mixed effects model, the variances of a subset of the random
    effects are equal to zero. There is no restriction on the subset of variances
    that can be tested: for example, it is possible to test that all the variances
    are equal to zero. Note that the implemented test is asymptotic.
    This package should be used on model fits from packages 'nlme', 'lmer', and 'saemix'.
    Charlotte Baey and Estelle Kuhn (2019) <doi:10.18637/jss.v107.i06>.
	"""
	
	homepage = "https://github.com/baeyc/varTestnlme/"
	cran = "varTestnlme" 

	version("1.3.5", md5="cd46a2a906e9ca78a9487ca5ce7d15cb")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-lmeresampler", type=("build", "run"))
	depends_on("r-alabama", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-merderiv", type=("build", "run"))
	depends_on("r-anocva", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-saemix", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
