# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSamur(RPackage):
	"""Stochastic Augmentation of Matched Data Using Restriction
Methods

	Augmenting a matched data set by generating multiple stochastic, matched samples from the data using a
  multi-dimensional histogram constructed from dropping the input matched data into a multi-dimensional grid built on
  the full data set. The resulting stochastic, matched sets will likely provide a collectively higher coverage of the full
  data set compared to the single matched set. Each stochastic match is without duplication, thus allowing downstream
  validation techniques such as cross-validation to be applied to each set without concern for overfitting.
	"""
	
	cran = "SAMUR" 

	version("1.1", md5="7c8bc523683dd367c0079d0a1bdeaa9a")

	depends_on("r-matching", type=("build", "run"))
