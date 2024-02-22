# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmridge(RPackage):
	"""Linear Ridge Regression with Ridge Penalty and Ridge Statistics

	Linear ridge regression coefficient's estimation and testing with different ridge related measures such as MSE, R-squared etc.
  REFERENCES
  i.   Hoerl and Kennard (1970) <doi:10.1080/00401706.1970.10488634>,
  ii.  Halawa and El-Bassiouni (2000) <doi:10.1080/00949650008812006>,
  iii. Imdadullah, Aslam, and Saima (2017),
  iv.  Marquardt (1970) <doi:10.2307/1267205>.
	"""
	
	cran = "lmridge" 

	version("1.2.2", md5="197ce8fdd149e7be6da3033f1b74c560")

	depends_on("r@3.4:", type=("build", "run"))
