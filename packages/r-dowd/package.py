# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDowd(RPackage):
	"""Functions Ported from 'MMR2' Toolbox Offered in Kevin Dowd's
Book Measuring Market Risk

	'Kevin Dowd's' book Measuring Market Risk is a widely read book 
          in the area of risk measurement by students and 
          practitioners alike. As he claims, 'MATLAB' indeed might have been the most 
          suitable language when he originally wrote the functions, but,
          with growing popularity of R it is not entirely 
	  valid. As 'Dowd's' code was not intended to be error free and were mainly 
	  for reference, some functions in this package have inherited those 
	  errors. An attempt will be made in future releases to identify and correct 
	  them. 'Dowd's' original code can be downloaded from www.kevindowd.org/measuring-market-risk/. 
          It should be noted that 'Dowd' offers both
          'MMR2' and 'MMR1' toolboxes. Only 'MMR2' was ported to R. 'MMR2' is more 
          recent version of 'MMR1' toolbox and they both have mostly similar 
          function. The toolbox mainly contains different parametric and non 
	  parametric methods for measurement of market risk as well as 
	  backtesting risk measurement methods.
	"""
	
	cran = "Dowd" 

	version("0.12", md5="1fbbf92bdce073f3a97920b3a819152e")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-bootstrap", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
