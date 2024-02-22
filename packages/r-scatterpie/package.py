# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScatterpie(RPackage):
	"""Scatter Pie Plot.

	Creates scatterpie plots, especially useful for plotting pies on a map."""

	cran = "scatterpie"

	version("0.2.1", md5="aa32b1425be7e6cda36f6cdb1d7401e9")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggfun", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
