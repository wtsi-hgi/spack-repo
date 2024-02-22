# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTinflex(RPackage):
	"""A Universal Non-Uniform Random Number Generator

	A universal non-uniform random number generator
  for quite arbitrary distributions with piecewise twice
  differentiable densities.
	"""
	
	cran = "Tinflex" 

	version("2.4", md5="e8a21e94284fcb679371382a31532f13")

