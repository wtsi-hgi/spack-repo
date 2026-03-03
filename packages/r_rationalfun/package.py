# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRationalfun(RPackage):
	"""Manipulation of Rational Functions

	Functions to manipulate rational functions, including basic
    arithmetic operators, derivatives, and integrals with EXPLICIT forms.
	"""
	
	homepage = "https://github.com/yixuan/rationalfun"
	cran = "rationalfun" 

	version("0.1-1", md5="1e8dfe2f611226d2d998496bc99273ea")

	depends_on("r-polynom", type=("build", "run"))
