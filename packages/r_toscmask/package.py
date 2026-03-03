# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RToscmask(RPackage):
	"""Improved Versions of Base Functions

	Operators and functions provided by base R sometimes lack some
    features found in other programming languages, such as the ability to
    concatenate strings using + or to repeat strings using *. This package aims
    at providing such functionality without breaking existing code, i.e., only
    statements, that would throw errors in pure base R are patched.
	"""
	
	cran = "toscmask" 

	version("1.2.3", md5="cdb574fc22e5def897b7c5d5566d1014")

