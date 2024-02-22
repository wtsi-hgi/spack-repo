# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTyped(RPackage):
	"""Support Types for Variables, Arguments, and Return Values

	A type system for R. It supports setting variable types in a script or the body of a function, so variables can't be assigned illegal values. Moreover it supports setting argument and return types for functions.
	"""
	
	homepage = "https://github.com/moodymudskipper/typed"
	cran = "typed" 

	version("0.0.1", md5="8055a5bbdd09d5d32526ac603d26b95f")

	depends_on("r-waldo", type=("build", "run"))
