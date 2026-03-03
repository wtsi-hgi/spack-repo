# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlroot(RPackage):
	"""searching for the root of equation

	This is a package which can help you search for the root
        of a equation.
	"""
	
	cran = "NLRoot" 

	version("1.0", md5="b904d8b6679fd0917467e46e9cb23f4b")

