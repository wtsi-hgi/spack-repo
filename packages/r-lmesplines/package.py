# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmesplines(RPackage):
	"""Add Smoothing Spline Modelling Capability to `nlme`

	Adds smoothing spline modelling capability to nlme. Fits
        smoothing spline terms in Gaussian linear and nonlinear
        mixed-effects models.
	"""
	
	cran = "lmeSplines" 

	version("1.1-12", md5="64253feba4296e868d30ee6ddb078cc4")

	depends_on("r-nlme@3.1.29:", type=("build", "run"))
