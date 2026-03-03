# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConicfit(RPackage):
	"""Algorithms for Fitting Circles, Ellipses and Conics Based on the
Work by Prof. Nikolai Chernov

	Geometric circle fitting with Levenberg-Marquardt (a, b, R), Levenberg-Marquardt reduced (a, b), Landau, Spath and Chernov-Lesort. Algebraic circle fitting with Taubin, Kasa, Pratt and Fitzgibbon-Pilu-Fisher. Geometric ellipse fitting with ellipse LMG (geometric parameters) and conic LMA (algebraic parameters). Algebraic ellipse fitting with Fitzgibbon-Pilu-Fisher and Taubin.
	"""
	
	cran = "conicfit" 

	version("1.0.4", md5="7d0be38f6477670c1259136a8587f085")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-geigen", type=("build", "run"))
