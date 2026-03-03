# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWeightedporttest(RPackage):
	"""Weighted Portmanteau Tests for Time Series Goodness-of-Fit

	An implementation of the Weighted Portmanteau Tests described
      in "New Weighted Portmanteau Statistics for Time Series Goodness-of-Fit Testing"
      published by the Journal of the American Statistical Association, Volume 107, 
      Issue 498, pages 777-787, 2012.
	"""
	
	cran = "WeightedPortTest" 

	version("1.1", md5="2709a342ccd3f29b7bc10de96f56329d")

