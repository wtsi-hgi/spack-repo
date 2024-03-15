# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgn(RPackage):
	"""Robust-Gauss Newton (RGN) Optimization of Sum-of-Squares
Objective Function

	Implementation of the Robust Gauss-Newton (RGN) algorithm,
    designed for solving optimization problems with a sum of least squares
    objective function. For algorithm details please refer to Qin et. al. (2018) 
    <doi:10.1029/2017WR022488>.
	"""
	
	homepage = "https://github.com/ClimateAnalytics/RGN/"
	cran = "RGN" 

	version("1.0.0", md5="8f2f56ec4e934857371a6c5face30931")

	depends_on("r@3.5:", type=("build", "run"))
