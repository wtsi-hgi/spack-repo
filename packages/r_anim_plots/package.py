# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnimPlots(RPackage):
	"""Simple Animated Plots for R

	Simple animated versions of basic R plots, using the 'animation'
    package. Includes animated versions of plot, barplot, persp, contour,
    filled.contour, hist, curve, points, lines, text, symbols, segments, and
    arrows.
	"""
	
	homepage = "https://github.com/hughjonesd/anim.plots"
	cran = "anim.plots" 

	version("0.2.2", md5="c577e49c1cbf95fbf8ef4a93fea94ff6")

	depends_on("r-animation", type=("build", "run"))
