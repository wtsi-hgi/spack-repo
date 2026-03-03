# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDcov(RPackage):
	"""A Fast Implementation of Distance Covariance

	Efficient methods for computing distance covariance and relevant statistics. See Székely et al.(2007) <doi:10.1214/009053607000000505>; Székely and Rizzo (2013) <doi:10.1016/j.jmva.2013.02.012>; Székely and Rizzo (2014) <doi:10.1214/14-AOS1255>; Huo and Székely (2016) <doi:10.1080/00401706.2015.1054435>.
	"""
	
	cran = "dcov" 

	version("0.1.1", md5="53a6fee26fc0ff913faa44bccebd3176")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
