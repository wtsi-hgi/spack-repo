# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgforce(RPackage):
	"""Accelerating 'ggplot2'.

	The aim of 'ggplot2' is to aid in visual data investigations. This focus
	has led to a lack of facilities for composing specialised plots. 'ggforce'
	aims to be a collection of mainly new stats and geoms that fills this gap.
	All additional functionality is aimed to come through the official
	extension system so using 'ggforce' should be a stable experience."""

	cran = "ggforce"

	license("MIT")

	version("0.4.2", md5="0ad559deefa799dd6c3f2688dc5a9484")

	depends_on("r-ggplot2@3.3.6:", type=("build", "run"))
	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-tweenr@0.1.5:", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-polyclip", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-systemfonts", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
