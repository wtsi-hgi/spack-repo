# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROceanview(RPackage):
	"""Visualisation of Oceanographic Data and Model Output

	Functions for transforming and viewing 2-D and 3-D (oceanographic) data and model output.
	"""
	
	cran = "OceanView" 

	version("1.0.7", md5="a2d3e3adc9fb056877f46cef5d449bf4")

	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-plot3drgl", type=("build", "run"))
	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-shape", type=("build", "run"))
