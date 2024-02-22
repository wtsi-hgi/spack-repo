# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmeln(RPackage):
	"""Estimation of Multinormal Mixture Distribution

	Fit multivariate mixture of normal distribution using
        covariance structure.
	"""
	
	cran = "mmeln" 

	version("1.5", md5="fa0edb37c943600bed9ac063f536e3dd")

