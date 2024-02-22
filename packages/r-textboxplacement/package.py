# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTextboxplacement(RPackage):
	"""Compute a Non-Overlapping Layout of Text Boxes to Label Multiple
Overlain Plots

	Compute a non-overlapping layout of text boxes to label multiple overlain curves. For each curve, iteratively search for an adjacent x,y position for the text box that does not overlap with the other curves. If this process fails, then offsets are computed to add to the y values for each curve, that results in sufficient space to add all of the text labels.
	"""
	
	cran = "textBoxPlacement" 

	version("1.0", md5="a9d7a03fdb48ab55f5cdaa5b0e86e564")

	depends_on("r@4.2:", type=("build", "run"))
