# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultipol(RPackage):
	"""Multivariate Polynomials

	Various utilities to manipulate multivariate polynomials.  The
    package is almost completely superceded by the 'spray' and 'mvp' packages,
    which are much more efficient.
	"""
	
	cran = "multipol" 

	version("1.0-9", md5="d3a4bfaf81932f44018a064c7ae3b5c8")

	depends_on("r-abind", type=("build", "run"))
