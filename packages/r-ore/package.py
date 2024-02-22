# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROre(RPackage):
	"""An R Interface to the Onigmo Regular Expression Library

	Provides an alternative to R's built-in functionality for handling
    regular expressions, based on the Onigmo library. Offers first-class
    compiled regex objects, partial matching and function-based substitutions,
    amongst other features.
	"""
	
	homepage = "https://github.com/jonclayden/ore"
	cran = "ore" 

	version("1.7.4.1", md5="cae052db6dbce48bb12fae5dc7c11343")

