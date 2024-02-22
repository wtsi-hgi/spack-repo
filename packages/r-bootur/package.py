# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBootur(RPackage):
	"""Bootstrap Unit Root Tests

	Set of functions to perform various bootstrap unit root tests for both individual time series
  (including augmented Dickey-Fuller test and union tests), multiple time series and panel data; see
  Smeekes and Wilms (2023) <doi:10.18637/jss.v106.i12>,
  Palm, Smeekes and Urbain (2008) <doi:10.1111/j.1467-9892.2007.00565.x>,
  Palm, Smeekes and Urbain (2011) <doi:10.1016/j.jeconom.2010.11.010>, 
  Moon and Perron (2012) <doi:10.1016/j.jeconom.2012.01.008>, 
  Smeekes and Taylor (2012) <doi:10.1017/S0266466611000387> and 
  Smeekes (2015) <doi:10.1111/jtsa.12110> for key references. 
	"""
	
	homepage = "https://github.com/smeekes/bootUR"
	cran = "bootUR" 

	version("1.0.3", md5="de3bdcf74e4d820ba78fea69e2e5e11f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-urca", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-parallelly", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppthread", type=("build", "run"))
