# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRadar(RPackage):
	"""Fundamental Formulas for Radar

	Fundamental formulas for Radar, for attenuation, range, velocity,
    effectiveness, power, scatter, doppler, geometry, radar equations, etc.
    Based on Nick Guy's Python package PyRadarMet
	"""
	
	cran = "radar" 

	version("1.0.0", md5="9ae8db05087af4b283dd6acc46a659ff")

	depends_on("r@2.7:", type=("build", "run"))
