# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpt5pl(RPackage):
	"""Optimal Designs for the 5-Parameter Logistic Model

	Obtain and evaluate various optimal designs for the 3, 4, and 5-parameter logistic models. The optimal designs are obtained based on the numerical algorithm in Hyun, Wong, Yang (2018) <doi:10.18637/jss.v083.i05>. 
	"""
	
	cran = "Opt5PL" 

	version("0.1.1", md5="21efbdf9c6a60dc9205a93ba20a92720")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
