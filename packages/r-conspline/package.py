# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConspline(RPackage):
	"""Partial Linear Least-Squares Regression using Constrained
Splines

	Given response y, continuous predictor x, and covariate matrix, the relationship between E(y) and x is estimated with a shape constrained regression spline.  Function outputs fits and various types of inference.
	"""
	
	cran = "ConSpline" 

	version("1.2", md5="b5736588c4e17ef1f5f16d02b53d36f5")

	depends_on("r-coneproj@1.12:", type=("build", "run"))
