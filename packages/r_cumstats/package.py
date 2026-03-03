# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCumstats(RPackage):
	"""Cumulative Descriptive Statistics

	Cumulative descriptive statistics for (arithmetic, geometric, harmonic) mean, median, mode, variance, skewness and kurtosis.
	"""
	
	cran = "cumstats" 

	version("1.0", md5="74943d432fc126e2fabfe4451febd00b")

