# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVcd(RPackage):
	"""Visualizing Categorical Data.

	Visualization techniques, data sets, summary and inference procedures aimed
	particularly at categorical data. Special emphasis is given to highly
	extensible grid graphics. The package was package was originally inspired
	by the book "Visualizing Categorical Data" by Michael Friendly and is now
	the main support package for a new book, "Discrete Data Analysis with R" by
	Michael Friendly and David Meyer (2015)."""

	cran = "vcd"

	license("GPL-2.0-only")

	version("1.4-12", md5="4f9a27422d6297399570a1a15bf868f9")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
