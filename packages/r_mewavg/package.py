# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMewavg(RPackage):
	"""A Fixed Memeory Moving Expanding Window Average

	Compute the average of a sequence of random vectors
  in a moving expanding window using a fixed amount of memory.
	"""
	
	cran = "mewAvg" 

	version("0.3.1", md5="ae12a4a49d03d21de092d81f14a4ed1d")

