# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCircnntsr(RPackage):
	"""Statistical Analysis of Circular Data using Nonnegative
Trigonometric Sums (NNTS) Models

	Includes functions for the analysis of circular data using distributions based on Nonnegative Trigonometric Sums (NNTS). The package includes functions for calculation of densities and distributions, for the estimation of parameters, for plotting and more.
	"""
	
	cran = "CircNNTSR" 

	version("2.3", md5="ec09acb385be9a8e9e121f1c24fc92c1")

