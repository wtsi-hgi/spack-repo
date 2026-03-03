# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLeafstar(RPackage):
	"""Silhouette to Area Ratio of Tilted Surfaces

	Implementation of trigonometric functions to calculate the exposure of flat, tilted surfaces, such as leaves and slopes, to direct solar radiation. It implements the equations in A.G. Escribano-Rocafort, A. Ventre-Lespiaucq, C. Granado-Yela, et al. (2014) <doi:10.1111/2041-210X.12141> in a few user-friendly R functions. All functions handle data obtained with 'Ahmes' 1.0 for Android, as well as more traditional data sources (compass, protractor, inclinometer). The main function (star()) calculates the potential exposure of flat, tilted surfaces to direct solar radiation (silhouette to area ratio, STAR). It is equivalent to the ratio of the leaf projected area to total leaf area, but instead of using area data it uses spatial position angles, such as pitch, roll and course, and information on the geographical coordinates, hour, and date. The package includes additional functions to recalculate STAR with custom settings of location and time, to calculate the tilt angle of a surface, and the minimum angle between two non-orthogonal planes.
	"""
	
	cran = "leafSTAR" 

	version("1.0", md5="4e4256fbea2663b839423cf97f04b086")

	depends_on("r@3.4.1:", type=("build", "run"))
