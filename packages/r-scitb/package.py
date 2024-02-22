# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScitb(RPackage):
	"""Provides Some Useful Functions for Making Statistical Tables

	You can use the functions provided by the package to make various statistical tables, 
             such as baseline data tables. Creates 'Table 1', i.e., a description of the baseline patient
             characteristics, which is essential in every medical research.
             Supports both continuous and categorical variables, as well as
             p-values and standardized mean differences.
             This method was described by Mary L McHugh (2013) <doi:10.11613/bm.2013.018>.
	"""
	
	cran = "scitb" 

	version("0.1.7", md5="af28a6abf9dedebf8391971872da5a0c")

	depends_on("r@3.50:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nortest", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
