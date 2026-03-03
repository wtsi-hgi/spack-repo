# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCleanr(RPackage):
	"""Helps You to Code Cleaner

	Check your R code for some of the most common
    layout flaws.  Many tried to teach us how to write code less dreadful,
    be it implicitly as B. W. Kernighan and D. M. Ritchie (1988)
    <ISBN:0-13-110362-8> in 'The C Programming Language' did, be it
    explicitly as R.C. Martin (2008) <ISBN:0-13-235088-2> in 'Clean Code:
    A Handbook of Agile Software Craftsmanship' did.  So we should check
    our code for files too long or wide, functions with too many lines,
    too wide lines, too many arguments or too many levels of nesting.
    Note: This is not a static code analyzer like pylint or the like.
    Checkout <https://cran.r-project.org/package=lintr> instead.
	"""
	
	homepage = "https://gitlab.com/fvafrcu/cleanr"
	cran = "cleanr" 

	version("1.4.0", md5="819c795777c13aebbbef3781f65a325d")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-fritools", type=("build", "run"))
	depends_on("r-pkgload", type=("build", "run"))
	depends_on("r-rprojroot", type=("build", "run"))
