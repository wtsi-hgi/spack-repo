# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIndeptest(RPackage):
	"""Nonparametric Independence Tests Based on Entropy Estimation

	Implementations of the weighted Kozachenko-Leonenko entropy estimator and independence tests based on this estimator, (Kozachenko and Leonenko (1987) <http://mi.mathnet.ru/eng/ppi797>). Also includes a goodness-of-fit test for a linear model which is an independence test between covariates and errors.
	"""
	
	cran = "IndepTest" 

	version("0.2.0", md5="148fe59bd56ba3209e9fe603fbbcb46f")

	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
