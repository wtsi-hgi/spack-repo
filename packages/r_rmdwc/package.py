# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmdwc(RPackage):
	"""Count Words, Chars and Non-Whitespace Chars in R Markdown Docs

	If you are using R Markdown documents then you have sometimes restrictions about the size of the documents, e.g. number of words, number of characters or non-whitespace characters. rmdcount() computes these counts with and without code chunks and returns the result as data frame.
	"""
	
	cran = "rmdwc" 

	version("0.3.0", md5="416c0fefd694aa0f47cc43a0007d0233")

	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
