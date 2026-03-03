# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCurry(RPackage):
	"""Partial Function Application with %<%, %-<%, and %><%

	Partial application is the process of reducing the arity of a
    function by fixing one or more arguments, thus creating a new function
    lacking the fixed arguments. The curry package provides three different ways
    of performing partial function application by fixing arguments from either
    end of the argument list (currying and tail currying) or by fixing multiple
    named arguments (partial application). This package provides this
    functionality through the %<%, %-<%, and %><% operators which allows for
    a programming style comparable to modern functional languages. Compared
    to other implementations such a purrr::partial() the operators in curry
    composes functions with named arguments, aiding in autocomplete etc.
	"""
	
	homepage = "https://github.com/thomasp85/curry"
	cran = "curry" 

	version("0.1.1", md5="a2d43da3367e9506e4e4e8a4523faaf5")

