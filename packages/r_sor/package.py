# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSor(RPackage):
	"""Estimation using Sequential Offsetted Regression

	Estimation for longitudinal data following outcome dependent sampling using the sequential offsetted regression technique.  Includes support for binary, count, and continuous data.  The first regression is a logistic regression, which uses a known ratio (the probability of being sampled given that the subject/observation was referred divided by the probability of being sampled given that the subject/observation was no referred) as an offset to estimate the probability of being referred given outcome and covariates.  The second regression uses this estimated probability to calculate the mean population response given covariates.
	"""
	
	cran = "SOR" 

	version("0.23.1", md5="cf87d8b180c50be9c9d2c010c96e4cb6")

	depends_on("r-matrix", type=("build", "run"))
