# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFaoutlier(RPackage):
	"""Influential Case Detection Methods for Factor Analysis and
Structural Equation Models

	Tools for detecting and summarize influential cases that
    can affect exploratory and confirmatory factor analysis models as well as
    structural equation models more generally (Chalmers, 2015, <doi:10.1177/0146621615597894>; 
    Flora, D. B., LaBrish, C. & Chalmers, R. P., 2012, <doi:10.3389/fpsyg.2012.00055>).
	"""
	
	homepage = "https://github.com/philchalmers/faoutlier"
	cran = "faoutlier" 

	version("0.7.6", md5="9107a0b93495c12cd4a6d1afaf48e3c4")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-sem", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-mirt@1.32.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pbapply@1.3.0:", type=("build", "run"))
