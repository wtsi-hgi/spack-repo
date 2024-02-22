# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCollinear(RPackage):
	"""Seamless Multicollinearity Management

	System for seamless management of multicollinearity in data frames
    with numeric and/or categorical variables for statistical analysis and 
    machine learning modeling. The package combines bivariate correlation 
    (Pearson, Spearman, and Cramer's V) with variance inflation factor analysis, 
    target encoding to transform categorical variables into numeric (Micci-Barreca, D. 2001 
    <DOI:10.1145/507533.507538>), and a flexible 
    feature prioritization method, to deliver a comprehensive 
    multicollinearity management tool covering a wide range of use cases.
	"""
	
	homepage = "https://blasbenito.github.io/collinear/"
	cran = "collinear" 

	version("1.1.1", md5="0d680248ee078b2ae18afda168179042")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
