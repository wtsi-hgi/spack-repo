# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfit(RPackage):
	"""Rank-Based Estimation for Linear Models

	Rank-based (R) estimation and inference for linear models.  Estimation
        is for general scores and a library of commonly used score
        functions is included.
	"""
	
	cran = "Rfit" 

	version("0.24.6", md5="ea52854410d99124abc8b45fae7c5781")

