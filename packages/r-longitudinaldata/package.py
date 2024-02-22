# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLongitudinaldata(RPackage):
	"""Longitudinal Data

	Tools for longitudinal data and joint longitudinal data (used by packages kml and kml3d).
	"""
	
	homepage = "https://www.r-project.org"
	cran = "longitudinalData" 

	version("2.4.5.1", md5="f5039fe9df8469379971c6c1b1aaeb8c")

	depends_on("r-clv", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-misc3d", type=("build", "run"))
