# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REattools(RPackage):
	"""Miscellaneous Functions for the Analysis of Educational
Assessments

	
   Miscellaneous functions for data cleaning and data analysis of educational assessments. Includes functions for descriptive 
   analyses, character vector manipulations and weighted statistics. Mainly a lightweight dependency for the packages 'eatRep', 
   'eatGADS', 'eatPrep' and 'eatModel' (which will be subsequently submitted to 'CRAN').
   The function for defining (weighted) contrasts in weighted effect coding refers to
   te Grotenhuis et al. (2017) <doi:10.1007/s00038-016-0901-1>.
   Functions for weighted statistics refer to
   Wolter (2007) <doi:10.1007/978-0-387-35099-8>.
	"""
	
	homepage = "https://github.com/weirichs/eatTools"
	cran = "eatTools" 

	version("0.7.5", md5="abd274bf0efca3c58082966797fa9762")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
