# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKeyboardsimulator(RPackage):
	"""Keyboard and Mouse Input Simulation for Windows OS

	Control your keyboard and mouse with R code by simulating key presses and mouse clicks. The input simulation is implemented with the Windows API.
	"""
	
	homepage = "https://github.com/ChiHangChen/KeyboardSimulator"
	cran = "KeyboardSimulator" 

	version("2.6.2", md5="9ec243b96e65eb76753bc274589521b7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
