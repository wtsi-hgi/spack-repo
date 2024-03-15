# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShape(RPackage):
	"""Functions for Plotting Graphical Shapes, Colors.

	Functions for plotting graphical shapes such as ellipses, circles,
	cylinders, arrows, ..."""

	cran = "shape"

	license("GPL-3.0-or-later")

	version("1.4.6.1", md5="42b7951c69b6c93178c07f2d189d0c89")

	depends_on("r@2.1:", type=("build", "run"))
