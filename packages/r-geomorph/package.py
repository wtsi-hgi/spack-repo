# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeomorph(RPackage):
	"""Geometric Morphometric Analyses of 2D/3D Landmark Data.

	Read, manipulate, and digitize landmark data, generate shape variables via
	Procrustes analysis for points, curves and surfaces, perform shape
	analyses, and provide graphical depictions of shapes and patterns of shape
	variation."""

	cran = "geomorph"

	version("4.0.6", md5="14c7cba5101d5593ba0653ba8debff14")

	depends_on("r-rrpp@1:", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
