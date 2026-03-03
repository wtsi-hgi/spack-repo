# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJcp(RPackage):
	"""Joint Change Point Detection

	Procedures for joint detection of changes in both expectation and variance in univariate sequences. Performs a statistical test of the null hypothesis of the absence of change points. In case of rejection performs an algorithm for change point detection. Reference - Bivariate change point detection - joint detection of changes in expectation and variance, Scandinavian Journal of Statistics, DOI 10.1111/sjos.12547.
	"""
	
	cran = "jcp" 

	version("1.2", md5="1e0298b94caac382182824150bf2a4e3")

