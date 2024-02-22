# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLogcondiscr(RPackage):
	"""Estimate a Log-Concave Probability Mass Function from Discrete
i.i.d. Observations

	Given independent and identically distributed observations X(1), ..., X(n), allows to compute the maximum likelihood estimator (MLE) of probability mass function (pmf) under the assumption that it is log-concave, see Weyermann (2007) and Balabdaoui, Jankowski, Rufibach, and Pavlides (2012). The main functions of the package are 'logConDiscrMLE' that allows computation of the log-concave MLE, 'logConDiscrCI' that computes pointwise confidence bands for the MLE, and 'kInflatedLogConDiscr' that computes a mixture of a log-concave PMF and a point mass at k.
	"""
	
	homepage = "http://www.kasparrufibach.ch"
	cran = "logcondiscr" 

	version("1.0.6", md5="6892b174ab156275f42a4c7b72956f48")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-cobs", type=("build", "run"))
