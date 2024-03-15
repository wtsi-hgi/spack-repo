# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REllipse(RPackage):
	"""Functions for Drawing Ellipses and Ellipse-Like Confidence Regions.

	Contains various routines for drawing ellipses and ellipse-like confidence
	regions, implementing the plots described in Murdoch and Chow (1996), A
	graphical display of large correlation matrices, The American Statistician
	50, 178-180. There are also routines implementing the profile plots
	described in Bates and Watts (1988), Nonlinear Regression Analysis and its
	Applications."""

	cran = "ellipse"

	license("GPL-2.0-or-later")

	version("0.5.0", md5="ebe98db0904bf2228bdc8c79ac19c665")

	depends_on("r@2:", type=("build", "run"))
