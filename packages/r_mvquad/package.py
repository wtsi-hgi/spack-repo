# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvquad(RPackage):
	"""Methods for Multivariate Quadrature

	Provides methods to construct multivariate grids, which can be used
    for multivariate quadrature. This grids can be based on different quadrature
    rules like Newton-Cotes formulas (trapezoidal-, Simpson's- rule, ...) or Gauss
    quadrature (Gauss-Hermite, Gauss-Legendre, ...). For the construction of the
    multidimensional grid the product-rule or the combination- technique can be
    applied.
	"""
	
	homepage = "https://github.com/weiserc/mvQuad/"
	cran = "mvQuad" 

	version("1.0-8", md5="3c4112ba39268e205c86332c77b53ff5")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
