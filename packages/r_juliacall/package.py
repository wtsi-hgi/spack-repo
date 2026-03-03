# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJuliacall(RPackage):
	"""Seamless Integration Between R and 'Julia'

	Provides an R interface to 'Julia',
    which is a high-level, high-performance dynamic programming language
    for numerical computing, see <https://julialang.org/> for more information.
    It provides a high-level interface as well as a low-level interface.
    Using the high level interface, you could call any 'Julia' function just like
    any R function with automatic type conversion. Using the low level interface,
    you could deal with C-level SEXP directly while enjoying the convenience of
    using a high-level programming language like 'Julia'.
	"""
	
	homepage = "https://github.com/Non-Contradiction/JuliaCall"
	cran = "JuliaCall" 

	version("0.17.5", md5="fdd420bebc118f7dc3e3e924ed747bdf")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-knitr@1.28:", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("julia@0.6.0:", type=("build", "link", "run"))
