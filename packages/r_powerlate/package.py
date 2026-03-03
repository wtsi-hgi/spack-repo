# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPowerlate(RPackage):
	"""Generalized Power Analysis for LATE

	An implementation of the generalized power analysis for the local average treatment effect (LATE), proposed by Bansak (2020) <doi:10.1214/19-STS732>. Power analysis is in the context of estimating the LATE (also known as the complier average causal effect, or CACE), with calculations based on a test of the null hypothesis that the LATE equals 0 with a two-sided alternative. The method uses standardized effect sizes to place a conservative bound on the power under minimal assumptions. Package allows users to recover power, sample size requirements, or minimum detectable effect sizes. Package also allows users to work with absolute effects rather than effect sizes, to specify an additional assumption to narrow the bounds, and to incorporate covariate adjustment.
	"""
	
	homepage = "https://github.com/kbansak/powerLATE"
	cran = "powerLATE" 

	version("0.1.1", md5="1d4ebb6412f64afb33de06300bb26c97")

