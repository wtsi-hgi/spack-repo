# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAplot(RPackage):
	"""Decorate a 'ggplot' with Associated Information.

	For many times, we are not just aligning plots as what 'cowplot' and
	'patchwork' did. Users would like to align associated information that
	requires axes to be exactly matched in subplots, e.g. hierarchical
	clustering with a heatmap. This package provides utilities to aligns
	associated subplots to a main plot at different sides (left, right, top and
	bottom) with axes exactly matched."""

	cran = "aplot"

	license("Artistic-2.0")

	version("0.2.2", md5="d71398cd2be0c5e51a46616471716348")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ggfun@0.1.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggplotify", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
