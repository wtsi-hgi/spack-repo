# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemtable(RPackage):
	"""Structural Equation Modeling Tables

	For confirmatory factor analysis ('CFA') and structural equation
             models ('SEM') estimated with the 'lavaan' package,
             this package provides functions to create model summary tables and model
             comparison tables for hypothesis testing. Tables can be produced in
             'LaTeX', 'HTML', or comma separated variables ('CSV'). 
	"""
	
	cran = "semTable" 

	version("1.8", md5="458f5bc90e5a197d22b7ea7574f86fe9")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-kutils", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-stationery", type=("build", "run"))
