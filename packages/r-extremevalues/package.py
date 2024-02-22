# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExtremevalues(RPackage):
	"""Univariate Outlier Detection

	Detect outliers in one-dimensional data.
	"""
	
	homepage = "https://github.com/markvanderloo/extremevalues"
	cran = "extremevalues" 

	version("2.3.4", md5="a596057a12e9349e7bad7ea48e16008b")

	depends_on("r@2.8:", type=("build", "run"))
	depends_on("r-gwidgets2", type=("build", "run"))
	depends_on("r-gwidgets2tcltk", type=("build", "run"))
