# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSignal(RPackage):
	"""Signal Processing

	A set of signal processing functions originally written for 'Matlab' and 'Octave'.
  Includes filter generation utilities, filtering functions,
  resampling routines, and visualization of filter models. It also
  includes interpolation functions.
	"""
	
	cran = "signal" 

	version("1.8-0", md5="b0d6578018b3f5bae98df615f997d70b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
