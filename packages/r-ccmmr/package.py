# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCcmmr(RPackage):
	"""Minimization of the Convex Clustering Loss Function

	Implements the convex clustering through majorization-minimization (CCMM) algorithm described in Touw, Groenen, and Terada (2022) <arXiv:2211.01877> to perform minimization of the convex clustering loss function.
	"""
	
	homepage = "https://github.com/djwtouw/CCMMR/"
	cran = "CCMMR" 

	version("0.2", md5="13b76dc1cee78126eda004a08bba0a66")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rann@2.6.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-r2r@0.1.1:", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
