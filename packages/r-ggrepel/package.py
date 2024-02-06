# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgrepel(RPackage):
	"""Repulsive Text and Label Geoms for 'ggplot2'.

	Provides text and label geoms for 'ggplot2' that help to avoid overlapping
	text labels. Labels repel away from each other and away from the data
	points."""

	cran = "ggrepel"

	version("0.9.5", md5="07e2c7cac82ce345ea35ca0522c72ea9")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang@0.3:", type=("build", "run"))
	depends_on("r-scales@0.5:", type=("build", "run"))
	depends_on("r-withr@2.5:", type=("build", "run"))
