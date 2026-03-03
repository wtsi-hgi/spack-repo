# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRwishart(RPackage):
	"""Random Wishart Matrix Generation

	An expansion of R's 'stats' random wishart matrix generation. 
  This package allows the user to generate singular, Uhlig and Harald (1994) 
  <doi:10.1214/aos/1176325375>, and pseudo wishart, Diaz-Garcia, et al.(1997) 
  <doi:10.1006/jmva.1997.1689>, matrices. In addition the user can generate 
  wishart matrices with fractional degrees of freedom, Adhikari (2008) 
  <doi:10.1061/(ASCE)0733-9399(2008)134:12(1029)>, commonly used in volatility 
  modeling. Users can also use this package to create random covariance matrices.
	"""
	
	homepage = "https://rwishart.bearstatistics.com"
	cran = "rWishart" 

	version("0.1.2", md5="353fec940f95a55666ea24782134e858")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
