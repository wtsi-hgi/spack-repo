# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSae2(RPackage):
	"""Small Area Estimation: Time-Series Models

	Time series area-level models for small area estimation. 
      The package supplements the functionality of the sae package.
      Specifically, it includes EBLUP fitting of the original Rao-Yu model, 
      which in the original form did not have a spatial component. The 
      package also offers a modified ('dynamic') version of the Rao-Yu model, 
      replacing the assumption of stationarity. Both univariate and 
      multivariate applications are supported. Of particular note is the 
      allowance for covariance of the area-level sample estimates over time, 
      as encountered in rotating panel designs such as the U.S. National 
      Crime Victimization Survey or present in a time-series of 5-year 
      estimates from the American Community Survey. Key references to the 
      methods include
      J.N.K. Rao and I. Molina (2015, ISBN:9781118735787),
      J.N.K. Rao and M. Yu (1994) <doi:10.2307/3315407>, and
      R.E. Fay and R.A. Herriot (1979) <doi:10.1080/01621459.1979.10482505>.
	"""
	
	cran = "sae2" 

	version("1.2-1", md5="7fe6ad1384b006aeb74e9262dbf5b9b1", url="https://cran.r-project.org/src/contrib/sae2_1.2-1.tar.gz")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
