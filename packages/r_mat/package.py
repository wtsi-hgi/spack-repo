# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMat(RPackage):
	"""Multidimensional Adaptive Testing

	Simulates Multidimensional Adaptive Testing using the multidimensional three-parameter logistic model as described in Segall (1996) <doi:10.1007/BF02294343>, van der Linden (1999) <doi:10.3102/10769986024004398>, Reckase (2009) <doi:10.1007/978-0-387-89976-3>, and Mulder & van der Linden (2009) <doi:10.1007/s11336-008-9097-5>.
	"""
	
	cran = "MAT" 

	version("2.3.1", md5="8d47ad7b7b9eb1ca0d8b5fa8d38bc71e")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
