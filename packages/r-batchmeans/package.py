# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBatchmeans(RPackage):
	"""Consistent Batch Means Estimation of Monte Carlo Standard Errors

	Provides consistent batch means estimation of Monte
    Carlo standard errors.
	"""
	
	cran = "batchmeans" 

	version("1.0-4", md5="345f227dc4c2e697efc7e80999635872")

