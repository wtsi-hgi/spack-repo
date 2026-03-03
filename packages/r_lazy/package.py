# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLazy(RPackage):
	"""Lazy Learning for Local Regression

	By combining constant, linear, and quadratic local models,
        lazy estimates the value of an unknown multivariate function on
        the basis of a set of possibly noisy samples of the function
        itself.  This implementation of lazy learning automatically
        adjusts the bandwidth on a query-by-query basis through a
        leave-one-out cross-validation.
	"""
	
	cran = "lazy" 

	version("1.2-18", md5="65a395896dae9c4ca7020a00bed3293d")

