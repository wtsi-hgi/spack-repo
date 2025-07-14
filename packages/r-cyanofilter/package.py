# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCyanofilter(RPackage):
	"""Phytoplankton Population Identification using Cell Pigmentation and/or Complexity

	An approach to filter out and/or identify phytoplankton cells from all particles measured via flow cytometry pigment and cell complexity information. It does this using a sequence of one-dimensional gates on pre-defined channels measuring certain pigmentation and complexity. The package is especially tuned for cyanobacteria, but will work fine for phytoplankton communities where there is at least one cell characteristic that differentiates every phytoplankton in the community.
	"""
	
	homepage = "https://github.com/fomotis/cyanoFilter"
	bioc = "cyanoFilter"

	version("1.16.0", commit="b0e1a35488445a821bf7ba997ad482280423b2be")
	version("1.10.0", commit="ccfe34009b92ad7d96a0de614b2d9d90cbaa9151")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-flowdensity", type=("build", "run"))
	depends_on("r-flowclust", type=("build", "run"))
	depends_on("r-cytometree", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-mrfdepth", type=("build", "run"))
