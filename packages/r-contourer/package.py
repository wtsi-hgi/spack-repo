# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RContourer(RPackage):
	"""Contouring of Non-Regular Three-Dimensional Data

	Create contour lines for a non regular series of points, potentially from a non-regular canvas.
	"""
	
	homepage = "http://contoureR.com"
	cran = "contoureR" 

	version("1.0.5", md5="6afdc5b7d3fa17119ec5f62524e7cb8b")

	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
