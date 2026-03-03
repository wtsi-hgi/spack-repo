# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobeth(RPackage):
	"""R Functions for Robust Statistics

	Locations problems, M-estimates of coefficients and scale
        in linear regression, Weights for bounded influence regression,
        Covariance matrix of the coefficient estimates, Asymptotic
        relative efficiency of regression M-estimates, Robust testing
        in linear models, High breakdown point regression, M-estimates
        of covariance matrices, M-estimates for discrete generalized
        linear models.
	"""
	
	cran = "robeth" 

	version("2.7-8", md5="396ba97f54528913619a21766452a074")

	depends_on("r@3.2:", type=("build", "run"))
