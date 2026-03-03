# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInterpolators(RPackage):
	"""Some Interpolation Methods

	Some interpolation methods taken from 'Boost': barycentric
    rational interpolation, modified Akima interpolation, PCHIP (piecewise
    cubic Hermite interpolating polynomial) interpolation, and Catmull-Rom
    splines.
	"""
	
	homepage = "https://github.com/stla/interpolators"
	cran = "interpolators" 

	version("1.0.1", md5="d4d74e53eb12191f5cea7c2ef61e14b7")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
