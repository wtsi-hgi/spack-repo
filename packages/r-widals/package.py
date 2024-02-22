# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWidals(RPackage):
	"""Weighting by Inverse Distance with Adaptive Least Squares

	Computationally easy modeling, interpolation, forecasting of massive temporal-spacial data.
	"""
	
	cran = "widals" 

	version("0.6.1", md5="261e73c655e9646b39be7df93f52515b")

	depends_on("r-snowfall", type=("build", "run"))
