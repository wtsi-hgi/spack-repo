# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlt(RPackage):
	"""A Nondecimated Lifting Transform for Signal Denoising

	Uses a modified lifting algorithm on which it builds the
        nondecimated lifting transform. It has applications in wavelet
        shrinkage.
	"""
	
	cran = "nlt" 

	version("2.2-1", md5="c026ce514448f6558be9a4420d27b57d")

	depends_on("r-ebayesthresh", type=("build", "run"))
	depends_on("r-adlift@1.3:", type=("build", "run"))
