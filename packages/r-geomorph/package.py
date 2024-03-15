# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
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

	license("GPL-3.0-or-later")

	version("4.0.7", md5="5fbf4145d6cf675fb7e41728edc6e9bd")

	depends_on("r-rrpp@2:", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
