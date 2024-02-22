# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RObre(RPackage):
	"""Optimal B-Robust Estimator Tools

	An implementation for computing Optimal B-Robust Estimators of two-parameter 
    distribution. The procedure is composed of some equations
    that are evaluated alternatively until the solution is reached. Some tools
    for analyzing the estimates are included. The most relevant is
    covariance matrix computation using a closed formula.
	"""
	
	cran = "OBRE" 

	version("0.2-0", md5="1dbfaf8679050d24779ec4a912762c6f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-pracma@1.7.3:", type=("build", "run"))
