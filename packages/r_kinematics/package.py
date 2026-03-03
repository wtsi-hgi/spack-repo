# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKinematics(RPackage):
	"""Studying Sampled Trajectories

	Allows analyzing time series representing two-dimensional movements.
    It accepts a data frame with a time (t), horizontal (x) and vertical (y) coordinate as columns,
    and returns several dynamical properties such as speed, acceleration or curvature.
	"""
	
	cran = "kinematics" 

	version("1.0.0", md5="c3c5c4dbfb8a1b55b66a603ea31195ed")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
