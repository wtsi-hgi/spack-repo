# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwitchcase(RPackage):
	"""A Simple and Flexible Switch-Case Construct for the 'R' Language

	Provides a switch-case construct for 'R', as it is known from other programming languages. It allows to test multiple, similar conditions in an efficient, easy-to-read manner, so nested if-else constructs can be avoided. The switch-case construct is designed as an 'R' function that allows to return values depending on which condition is met and lets the programmer flexibly decide whether or not to leave the switch-case construct after a case block has been executed.
	"""
	
	homepage = "https://github.com/jsugarelli/switchcase/"
	cran = "switchcase" 

	version("0.1.1", md5="3410269ea052a63d424103a592672203")

