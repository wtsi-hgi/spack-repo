# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMonopoly(RPackage):
	"""Functions to Fit Monotone Polynomials

	Functions for fitting monotone polynomials to data.
             Detailed discussion of the methodologies used can be
             found in Murray, Mueller and Turlach (2013)
             <doi:10.1007/s00180-012-0390-5> and Murray, Mueller and
             Turlach (2016) <doi:10.1080/00949655.2016.1139582>.  
	"""
	
	cran = "MonoPoly" 

	version("0.3-10", md5="da3b4ef63ab814bcb7b911ffe73ca9ee")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
