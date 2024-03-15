# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RViridislite(RPackage):
	"""Colorblind-Friendly Color Maps (Lite Version).

	Color maps designed to improve graph readability for readers with common
	forms of color blindness and/or color vision deficiency. The color maps are
	also perceptually-uniform, both in regular form and also when converted to
	black-and-white for printing. This is the 'lite' version of the 'viridis'
	package that also contains 'ggplot2' bindings for discrete and continuous
	color and fill scales and can be found at
	<https://cran.r-project.org/package=viridis>."""

	cran = "viridisLite"

	version("0.4.2", md5="059e754e58fd6735dd50a1799f95c8c1")

	depends_on("r@2.10:", type=("build", "run"))
