# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGafit(RPackage):
	"""Genetic Algorithm for Curve Fitting

	A group of sample points are evaluated against a
        user-defined expression, the sample points are lists of
        parameters with values that may be substituted into that
        expression. The genetic algorithm attempts to make the result
        of the expression as low as possible (usually this would be the
        sum of residuals squared).
	"""
	
	homepage = "http://lnx-bsp.net/"
	cran = "gafit" 

	version("0.5.1", md5="612bfb38d13ddb682cd3800648a55f70")

	depends_on("r@3:", type=("build", "run"))
