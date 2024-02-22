# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrenchcurve(RPackage):
	"""Generate Open or Closed Interpolating Curves

	Functions for finding smooth interpolating curves connecting
    a series of points in the plane.  Curves may be open or closed,
    that is, with the first and last point of the curve at the initial point.
	"""
	
	cran = "frenchCurve" 

	version("0.2.0", md5="1d426e2458e3ffbc684c4ea9a0eb5109")

	depends_on("r-sp", type=("build", "run"))
