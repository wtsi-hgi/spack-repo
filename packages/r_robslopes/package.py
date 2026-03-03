# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobslopes(RPackage):
	"""Fast Algorithms for Robust Slopes

	Fast algorithms for the Theil-Sen estimator,
  Siegel's repeated median slope estimator, and Passing-Bablok regression.
  The implementation is based on algorithms by
  Dillencourt et. al (1992) <doi:10.1142/S0218195992000020> and Matousek et. al (1998)  <doi:10.1007/PL00009190>.
  The implementations are detailed in 
  Raymaekers (2023) <doi:10.32614/RJ-2023-012> and 
  Raymaekers J., Dufey F. (2022) <arXiv:2202.08060>.
  All algorithms run in quasilinear time.
	"""
	
	cran = "robslopes" 

	version("1.1.3", md5="31b7009d1f6a74e59ede22c4e2192cad")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
