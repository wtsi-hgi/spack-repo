# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGetdteval(RPackage):
	"""Translating Coding Statements using get() and eval() for
Improved Run-Time Coding Efficiency

	The getDTeval() function facilitates the translation of the original coding statement to an optimized form for improved runtime efficiency without compromising on the programmatic coding design.
    The function can either provide a translation of the coding statement, directly evaluate the translation to return a coding result, or provide both of these outputs.
	"""
	
	cran = "getDTeval" 

	version("0.0.2", md5="c911968c0ee8eb34becb17bc780b08db")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-formulaic", type=("build", "run"))
	depends_on("r-microbenchmark", type=("build", "run"))
