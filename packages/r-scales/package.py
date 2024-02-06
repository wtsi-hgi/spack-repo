# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScales(RPackage):
	"""Scale Functions for Visualization.

	Graphical scales map data to aesthetics, and provide methods for
	automatically determining breaks and labels for axes and legends."""

	cran = "scales"

	version("1.3.0", md5="eeaf1b6727eceab473f4c139e99601c8")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-farver@2.0.3:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-labeling", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-munsell@0.5:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
