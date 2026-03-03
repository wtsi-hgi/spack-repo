# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHistmdl(RPackage):
	"""A Most Informative Histogram-Like Model

	Using the MDL principle, it is possible to estimate
	parameters for a histogram-like model. The package contains
	the implementation of such an estimation method.
	"""
	
	cran = "histmdl" 

	version("0.7-1", md5="4e2219fd7542d1b13ba052dd44f102c5")

