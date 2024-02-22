# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChangepointsvar(RPackage):
	"""Change-Points Detections for Changes in Variance

	Detection of change-points for variance of heteroscedastic Gaussian variables with piecewise constant variance function. Adelfio, G. (2012), Change-point detection for variance piecewise constant models, Communications in Statistics, Simulation and Computation, 41:4, 437-448, <doi:10.1080/03610918.2011.592248>.
	"""
	
	cran = "changepointsVar" 

	version("0.1.1", md5="cb2d55dc9983fbf9dd1ed05d0aee34d3")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lars", type=("build", "run"))
