# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInlinedocs(RPackage):
	"""Convert Inline Comments to Documentation

	Generates Rd files from R source code with comments.
 The main features of the default syntax are that
 (1) docs are defined in comments near the relevant code,
 (2) function argument names are not repeated in comments, and
 (3) examples are defined in R code, not comments.
 It is also easy to define a new syntax.
	"""
	
	homepage = "https://github.com/tdhock/inlinedocs"
	cran = "inlinedocs" 

	version("2023.9.4", md5="3df2087df03fce0ef6c62365f4d2fb41")

	depends_on("r@2.9:", type=("build", "run"))
