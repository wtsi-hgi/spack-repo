# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoefa(RPackage):
	"""Meta Analysis of Factor Analysis Based on CO-Occurrence Matrices

	Provide a series of functions to conduct a meta analysis of 
    factor analysis based on co-occurrence matrices. The tool can be used to 
    solve the factor structure (i.e. inner structure of a construct, or scale) 
    debate in several disciplines, such as psychology, psychiatry, management, 
    education so on. References: Shafer (2005) <doi:10.1037/1040-3590.17.3.324>; 
    Shafer (2006) <doi:10.1002/jclp.20213>; Loeber and Schmaling (1985) <doi:10.1007/BF00910652>.
	"""
	
	cran = "coefa" 

	version("1.0.3", md5="e8ace231f37ad92225175734d966ea26")

	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
