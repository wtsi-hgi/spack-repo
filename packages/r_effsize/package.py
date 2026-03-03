# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REffsize(RPackage):
	"""Efficient Effect Size Computation

	A collection of functions to compute the standardized 
  effect sizes for experiments (Cohen d, Hedges g, Cliff delta, Vargha-Delaney A). 
  The computation algorithms have been optimized to allow efficient computation even 
  with very large data sets.
	"""
	
	homepage = "https://github.com/mtorchiano/effsize/"
	cran = "effsize" 

	version("0.8.1", md5="83ccdd795b41c2284cdc668dfc5cd0f3")

