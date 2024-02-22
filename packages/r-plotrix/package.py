# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlotrix(RPackage):
	"""Various Plotting Functions.

	Lots of plots, various labeling, axis and color scaling functions."""

	cran = "plotrix"

	version("3.8-4", md5="553079f4dd3f183030b5157ae00cb5ae")

	depends_on("r@3.5:", type=("build", "run"))
