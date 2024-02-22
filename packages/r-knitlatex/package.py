# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKnitlatex(RPackage):
	"""'Knitr' Helpers - Mostly Tables

	Provides several helper functions for working with 'knitr' and 'LaTeX'.
  It includes 'xTab' for creating traditional 'LaTeX' tables, 'lTab' for generating
  'longtable' environments, and 'sTab' for generating a 'supertabular' environment.
  Additionally, this package contains a knitr_setup() function which fixes a
  well-known bug in 'knitr', which distorts the 'results="asis"' command when used
  in conjunction with user-defined commands; and a com command (<<com=TRUE>>=)
  which renders the output from 'knitr' as a 'LaTeX' command.
	"""
	
	cran = "knitLatex" 

	version("0.9.0", md5="ee61d56a00deefc0bbba8fdcbd6c80a5")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-knitr@1.10.5:", type=("build", "run"))
