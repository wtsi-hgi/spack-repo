# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShades(RPackage):
	"""Simple Colour Manipulation

	Functions for easily manipulating colours, creating colour scales and calculating colour distances.
	"""
	
	homepage = "https://github.com/jonclayden/shades"
	cran = "shades" 

	version("1.4.0", md5="84eb1e60ab7bc6d1fbbd662840230951")

