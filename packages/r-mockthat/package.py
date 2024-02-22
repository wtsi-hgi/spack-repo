# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMockthat(RPackage):
	"""Function Mocking for Unit Testing

	With the deprecation of mocking capabilities shipped with
    'testthat' as of 'edition 3' it is left to third-party packages to replace
    this functionality, which in some test-scenarios is essential in order to
    run unit tests in limited environments (such as no Internet connection).
    Mocking in this setting means temporarily substituting a function with a
    stub that acts in some sense like the original function (for example by
    serving a HTTP response that has been cached as a file). The only exported
    function 'with_mock()' is modeled after the eponymous 'testthat' function
    with the intention of providing a drop-in replacement.
	"""
	
	homepage = "https://nbenn.github.io/mockthat/"
	cran = "mockthat" 

	version("0.2.8", md5="7649c69b1876895f6753f26aa506256f")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
