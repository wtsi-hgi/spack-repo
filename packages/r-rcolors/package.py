# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcolors(RPackage):
	"""270 'NCL' Color Tables in R Language

	'NCL' (NCAR Command Language) is one of the most popular spatial 
    data mapping tools in meteorology studies, due to its beautiful output 
    figures with plenty of color palettes designed by experts 
    <https://www.ncl.ucar.edu/index.shtml>. 
    Here we translate all 'NCL' color palettes into R hexadecimal RGB colors and 
    provide color selection function, which will help users make a beautiful figure.
	"""
	
	cran = "rcolors" 

	version("0.1.0", md5="0cc278dda752d0c22685a252067a032e")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
