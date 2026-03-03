# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPmr(RPackage):
	"""Probability Models for Ranking Data

	Descriptive statistics (mean rank, pairwise frequencies, and marginal matrix), Analytic Hierarchy Process models (with Saaty's and Koczkodaj's inconsistencies), probability models (Luce models, distance-based models, and rank-ordered logit models) and visualization with multidimensional preference analysis for ranking data are provided. Current, only complete rankings are supported by this package.
	"""
	
	cran = "pmr" 

	version("1.2.5.1", md5="7d54dd3ddfeceae8afcc1f3fda642c4d")

