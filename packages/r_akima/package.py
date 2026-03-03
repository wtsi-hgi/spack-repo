# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAkima(RPackage):
	"""Interpolation of Irregularly and Regularly Spaced Data

	Several cubic spline interpolation methods of H. Akima for irregular and
  regular gridded data are available through this package, both for the bivariate case
  (irregular data: ACM 761, regular data: ACM 760) and univariate case (ACM 433 and ACM 697).
  Linear interpolation of irregular gridded data is also covered by reusing D. J. Renkas
  triangulation code which is part of Akimas Fortran code. A bilinear interpolator
  for regular grids was also added for comparison with the bicubic interpolator on
  regular grids.
	"""
	
	cran = "akima" 

	version("0.6-3.4", md5="55d36a85ecb1c2f82d22bdcec6f9ee3e")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
