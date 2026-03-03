# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFunprog(RPackage):
	"""Functional Programming

	
    High-order functions for data manipulation : sort or group data, given one
    or more auxiliary functions. Functions are inspired by other pure
    functional programming languages ('Haskell' mainly). The package also 
    provides built-in function operators for creating compact anonymous
    functions, as well as the possibility to use the 'purrr' package syntax.
	"""
	
	homepage = "https://py_b.gitlab.io/funprog"
	cran = "funprog" 

	version("0.3.0", md5="9c332346bb7a66c12a09a599331d7fd1")

