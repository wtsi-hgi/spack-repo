# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMandalar(RPackage):
	"""Building Mandalas from Parametric Equations of Classical Curves

	Provides an algorithm for creating mandalas. From the perspective of classic mathematical curves and rigid movements on the plane, the package allows you to select curves and produce mandalas from the curve. The algorithm was developed based on the book by Alcoforado et. al. entitled "Art, Geometry and Mandalas with R" (2022) in press by the USP Open Books Portal.
	"""
	
	homepage = "https://lucianealcoforado.shinyapps.io/Mandala/"
	cran = "MandalaR" 

	version("0.1.0", md5="bda87d0bbc0281a0d8a745db211f21b3")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
