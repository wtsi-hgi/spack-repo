# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTinytable(RPackage):
	"""Simple and Configurable Tables in 'HTML', 'LaTeX', 'Markdown',
'Word', 'PNG', 'PDF', and 'Typst' Formats

	Create highly customized tables with this simple and dependency-free package. Data frames can be converted to 'HTML', 'LaTeX', 'Markdown', 'Word', 'PNG', 'PDF', or 'Typst' tables. The user interface is minimalist and easy to learn. The syntax concise. 'HTML' tables can be customized using the flexible 'Bootstrap' framework, and 'LaTeX' code with the 'tabularray' package.
	"""
	
	homepage = "https://vincentarelbundock.github.io/tinytable/"
	cran = "tinytable" 

	version("0.2.1", md5="33dde0eeb785de7cd622cc461b5b048c")

	depends_on("r@4.1:", type=("build", "run"))
