# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvhtests(RPackage):
	"""Multivariate Hypothesis Tests

	Hypothesis tests for multivariate data. Tests for one and two mean vectors, multivariate analysis of variance, tests for one, two or more covariance matrices. References include: Mardia K.V., Kent J.T. and Bibby J.M. (1979). Multivariate Analysis. ISBN: 978-0124712522. London: Academic Press.
	"""
	
	cran = "mvhtests" 

	version("1.0", md5="3bb48f613eafdd8b3bccacc97653a4ce")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-emplik", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-rfast2", type=("build", "run"))
