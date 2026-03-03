# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMarkowitzr(RPackage):
	"""Statistical Significance of the Markowitz Portfolio

	A collection of tools for analyzing significance of 
    Markowitz portfolios, using the delta method on the second moment
    matrix, <arxiv:1312.0557>.
	"""
	
	homepage = "https://github.com/shabbychef/MarkowitzR"
	cran = "MarkowitzR" 

	version("1.0.3", md5="dd13b52b2350b3367b50dc3a5aa618f5")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
