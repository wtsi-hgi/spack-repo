# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTexcheckr(RPackage):
	"""Parses LaTeX Documents for Errors

	Checks LaTeX documents and .bib files for typing errors, such as spelling errors, incorrect quotation marks. Also provides useful functions for parsing and linting bibliography files.
	"""
	
	homepage = "https://github.com/HughParsonage/TeXCheckR"
	cran = "TeXCheckR" 

	version("0.8.1", md5="ca56acc30d8f860bb7ef496131c15548")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-clisymbols", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-data-table@1.9:", type=("build", "run"))
	depends_on("r-fastmatch", type=("build", "run"))
	depends_on("r-hunspell@2.5:", type=("build", "run"))
	depends_on("r-hutils@0.8:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
