# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGatepoints(RPackage):
	"""Easily Gate or Select Points on a Scatter Plot

	Allows user to choose/gate a region on the plot and returns points
    within it.
	"""
	
	homepage = "https://github.com/wjawaid/gatepoints"
	cran = "gatepoints" 

	version("0.1.5", md5="8e28707552829e53f331f11017de8b42")

	depends_on("r@3:", type=("build", "run"))
