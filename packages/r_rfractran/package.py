# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfractran(RPackage):
	"""A 'FRACTRAN' Interpreter and Some Helper Functions

	'FRACTRAN' is an obscure yet tantalizing programming language invented by John Conway of 'Game of Life' fame. The code consists of a sequence of fractions. The rules are simple. First, select an integer to initialize the process. Second, multiply the integer by the first fraction. If an integer results, start again with the new integer. If not, try the next fraction. Finally, if no such multiplication yields an integer, terminate the program. For more information, see <https://en.wikipedia.org/wiki/FRACTRAN> . 
	"""
	
	cran = "Rfractran" 

	version("1.0.1", md5="5596bef9593335c9cf9604e79299460b")

	depends_on("r-gmp", type=("build", "run"))
