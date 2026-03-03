# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPbrackets(RPackage):
	"""Plot Brackets

	Adds different kinds of brackets to a plot, including braces, chevrons, parentheses or square brackets.
	"""
	
	cran = "pBrackets" 

	version("1.0.1", md5="bf42d31fc34f8db238cdcba0cf4288da")

	depends_on("r@4:", type=("build", "run"))
