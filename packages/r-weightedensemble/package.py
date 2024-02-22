# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWeightedensemble(RPackage):
	"""Weighted Ensemble for Hybrid Model

	The weighted ensemble method is a valuable approach for combining forecasts. This algorithm employs several optimization techniques to generate optimized weights. This package has been developed using algorithm of Armstrong (1989) <doi:10.1016/0024-6301(90)90317-W>.
	"""
	
	cran = "WeightedEnsemble" 

	version("0.1.0", md5="908b65055f8f6db897d4152a85f2d9da")

	depends_on("r-metaheuristicopt", type=("build", "run"))
