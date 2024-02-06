# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RViridis(RPackage):
	"""Colorblind-Friendly Color Maps for R.

	Color maps designed to improve graph readability for readers with common
	forms of color blindness and/or color vision deficiency. The color maps are
	also perceptually-uniform, both in regular form and also when converted to
	black-and-white for printing. This package also contains 'ggplot2' bindings
	for discrete and continuous color and fill scales. A lean version of the
	package called 'viridisLite' that does not include the 'ggplot2' bindings
	can be found at <https://cran.r-project.org/package=viridisLite>."""

	cran = "viridis"

	version("0.6.5", md5="d3379572b7c9e31148c52c8e85417d9e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-viridislite@0.4:", type=("build", "run"))
	depends_on("r-ggplot2@1.0.1:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
