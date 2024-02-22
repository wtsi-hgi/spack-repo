# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RContfrac(RPackage):
	"""Continued Fractions

	Various utilities for evaluating continued fractions.
	"""
	
	homepage = "https://github.com/RobinHankin/contfrac.git"
	cran = "contfrac" 

	version("1.1-12", md5="8859a0eda910d18eb97683b535d2dc1d")

