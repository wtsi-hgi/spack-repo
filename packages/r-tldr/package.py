# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTldr(RPackage):
	"""T Loux Doing R: Functions to Simplify Data Analysis and
Reporting

	Gives a number of functions to aid common data 
    analysis processes and reporting statistical results in an 'RMarkdown' file. 
    Data analysis functions combine multiple base R functions used to describe 
    simple bivariate relationships into a single, easy to use function. 
    Reporting functions will return character strings to report p-values, 
    confidence intervals, and hypothesis test and regression results. Strings 
    will be LaTeX-formatted as necessary and will knit pretty in an 'RMarkdown' 
    document. The package also provides a wrapper for the CreateTableOne() 
    function in the 'tableone' package to make the results knit-able.
	"""
	
	cran = "tldr" 

	version("0.3.0", md5="952ad04d8cd193dee1f20211a8c82437")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-tableone", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
