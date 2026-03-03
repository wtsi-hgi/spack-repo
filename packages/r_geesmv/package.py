# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeesmv(RPackage):
	"""Modified Variance Estimators for Generalized Estimating
Equations

	Generalized estimating equations with the original sandwich variance estimator proposed by Liang and Zeger (1986), and eight types of more recent modified variance estimators for improving the finite small-sample performance.
	"""
	
	cran = "geesmv" 

	version("1.3", md5="1c34d222b363b85a6aac562a637c367b")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-gee", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
