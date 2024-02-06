# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPatchwork(RPackage):
	"""The Composer of Plots.

	The 'ggplot2' package provides a strong API for sequentially building up a
	plot, but does not concern itself with composition of multiple plots.
	'patchwork' is a package that expands the API to allow for arbitrarily
	complex composition of plots by, among others, providing mathematical
	operators for combining multiple plots. Other packages that try to address
	this need (but with a different approach) are 'gridExtra' and 'cowplot'."""

	cran = "patchwork"

	version("1.2.0", md5="3cf908b531cf600341be463a542a6e6e")

	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
