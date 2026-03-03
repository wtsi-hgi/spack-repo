# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpec(RPackage):
	"""Root Mean Square Curvature Calculation

	Calculates the RMS intrinsic and parameter-effects curvatures of a nonlinear regression model. The curvatures are global measures of assessing whether a model/data set combination is close-to-linear or not. See Bates and Watts (1980) <doi:10.1002/9780470316757> and Ratkowsky and Reddy (2017) <doi:10.1093/aesa/saw098> for details.  
	"""
	
	cran = "IPEC" 

	version("1.1.0", md5="ab24eb9408972262447eae3c49c5c8c5")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-numderiv@2016.8.1.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
