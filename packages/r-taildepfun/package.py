# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTaildepfun(RPackage):
	"""Minimum Distance Estimation of Tail Dependence Models

	Provides functions implementing minimal distance estimation methods for parametric tail dependence models, as proposed in  
	 Einmahl, J.H.J., Kiriliouk, A., Krajina, A., and Segers, J. (2016) <doi:10.1111/rssb.12114> and 
	 Einmahl, J.H.J., Kiriliouk, A., and Segers, J. (2018) <doi:10.1007/s10687-017-0303-7>.
	"""
	
	cran = "tailDepFun" 

	version("1.0.1", md5="22268a0042077c2096e8ddb4bd620c1c")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-spatialextremes", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
