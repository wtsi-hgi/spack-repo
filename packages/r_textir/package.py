# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTextir(RPackage):
	"""Inverse Regression for Text Analysis

	Multinomial (inverse) regression inference for text documents and associated attributes.  For details see: Taddy (2013 JASA) Multinomial Inverse Regression for Text Analysis <arXiv:1012.2098> and Taddy (2015, AoAS), Distributed Multinomial Regression, <arXiv:1311.6139>. A minimalist partial least squares routine is also included.  Note that the topic modeling capability of earlier 'textir' is now a separate package, 'maptpx'.
	"""
	
	homepage = "http://taddylab.com"
	cran = "textir" 

	version("2.0-5", md5="7b84c9b10ba9221304ef5df5cdef9004")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-distrom", type=("build", "run"))
	depends_on("r-gamlr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
