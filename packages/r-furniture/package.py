# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFurniture(RPackage):
	"""Furniture for Quantitative Scientists

	Contains four main functions (i.e., four pieces of furniture):
    table1() which produces a well-formatted table of descriptive statistics common as Table 1
    in research articles, tableC() which produces a well-formatted table of correlations,
    tableF() which provides frequency counts, and washer() which 
    is helpful in cleaning up the data. These furniture-themed functions are designed 
    to simplify common tasks in quantitative analysis. Other data summary and cleaning tools 
    are also available.
	"""
	
	cran = "furniture" 

	version("1.9.14", md5="7372acb67b3251b8eb7d9afd06bf1de7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
