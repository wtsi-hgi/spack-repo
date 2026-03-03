# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLfdrMle(RPackage):
	"""Estimation of the Local False Discovery Rates by Type II Maximum
Likelihood Estimation

	Suite of R functions for the estimation of the local false discovery rate (LFDR) using Type II maximum likelihood estimation (MLE).
	"""
	
	homepage = "http://www.cran.r-project.org"
	cran = "LFDR.MLE" 

	version("1.0.1", md5="0be7b44b2fa2a49e203bb33179b1f5e0")

