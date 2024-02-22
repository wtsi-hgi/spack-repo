# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStddiff(RPackage):
	"""Calculate the Standardized Difference for Numeric, Binary and
Category Variables

	Contains three main functions including
  stddiff.numeric(), stddiff.binary() and stddiff.category().
  These are used to calculate the standardized difference between two groups.
  It is especially used to evaluate the balance between two groups
  before and after propensity score matching.
	"""
	
	cran = "stddiff" 

	version("3.1", md5="3347f0fbc9f00ce4c84427e48edf76d5")

