# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPortes(RPackage):
	"""Portmanteau Tests for Time Series Models

	Contains common univariate and multivariate portmanteau test statistics for time series models. These tests are based on using asymptotic distributions such as chi-square distribution and based on using the Monte Carlo significance tests. Also, it can be used to simulate from univariate and multivariate seasonal time series models.
	"""
	
	cran = "portes" 

	version("6.0", md5="64d0bf52f043d4fa09ed2ed0ec1d6e97")

	depends_on("r-forecast@8.21:", type=("build", "run"))
	depends_on("r-vars@1.5.9:", type=("build", "run"))
