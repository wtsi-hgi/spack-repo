# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMro(RPackage):
	"""Multiple Correlation

	Computes multiple correlation coefficient when the data matrix is given and tests its significance.
	"""
	
	cran = "mro" 

	version("0.1.1", md5="871f5bf7171372bc2833ebd83227c049")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
