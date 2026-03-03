# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdapsamp(RPackage):
	"""Adaptive Sampling Algorithms

	For distributions whose probability density functions are log-concave, the adaptive rejection sampling algorithm can be used to build envelope functions for sampling. For others, we can use the modified adaptive rejection sampling algorithm, the concave-convex adaptive rejection sampling algorithm and the adaptive slice sampling algorithm. So we designed an R package mainly including 4 functions: rARS(), rMARS(), rCCARS() and rASS(). These functions can realize sampling based on the algorithms above.
	"""
	
	cran = "AdapSamp" 

	version("1.1.1", md5="1b50c4e7187ef2c0c9637f677567c689")

	depends_on("r-pracma", type=("build", "run"))
