# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFormatdown(RPackage):
	"""Formatting Tools for 'rmarkdown' Documents

	Provides a small set of tools for formatting tasks when creating 
    documents in R Markdown or Quarto Markdown. Convert the elements of a 
    numerical vector to character strings in one of several forms: powers-of-ten 
    notation in engineering or scientific form delimited for rendering as inline 
    equations; integer or decimal notation delimited for equation rendering; 
    numbers with measurement units (non-delimited) where units are selected to 
    eliminate the need for powers-of-ten or scientific notation. Useful for 
    rendering a numerical scalar in an inline R code chunk as well as formatting 
    columns of data frames displayed in a table. 
	"""
	
	homepage = "https://github.com/graphdr/formatdown/"
	cran = "formatdown" 

	version("0.1.3", md5="29fe3c4618b93e96f41ed647d462d400")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-wrapr", type=("build", "run"))
