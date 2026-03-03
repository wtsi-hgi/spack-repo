# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorrgram(RPackage):
	"""Plot a Correlogram

	Calculates correlation of variables and displays the results
    graphically. Included panel functions can display points, shading, ellipses, and
    correlation values with confidence intervals. See Friendly (2002) <doi:10.1198/000313002533>.
	"""
	
	homepage = "https://kwstat.github.io/corrgram/"
	cran = "corrgram" 

	version("1.14", md5="a8bf8378b6eecabc911e4d7ca35c573c")

