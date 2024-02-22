# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSkewt(RPackage):
	"""The Skewed Student-t Distribution

	Density, distribution function, quantile function and
        random generation for the skewed t distribution of Fernandez
        and Steel.
	"""
	
	cran = "skewt" 

	version("1.0", md5="1f57e45feb639a2445b3342e990f5f41")

