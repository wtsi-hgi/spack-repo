# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAcss(RPackage):
	"""Algorithmic Complexity for Short Strings

	Main functionality is to provide the algorithmic complexity for
    short strings, an approximation of the Kolmogorov Complexity of a short
    string using the coding theorem method (see ?acss). The database containing
    the complexity is provided in the data only package acss.data, this package
    provides functions accessing the data such as prob_random returning the
    posterior probability that a given string was produced by a random process.
    In addition, two traditional (but problematic) measures of complexity are
    also provided: entropy and change complexity.
	"""
	
	homepage = "http://complexitycalculator.com/methodology.html"
	cran = "acss" 

	version("0.2-5", md5="98e6b46a04e3c9f1505de3b63c85e2d8")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-acss-data", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
