# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClassint(RPackage):
	"""Choose Univariate Class Intervals.

	Selected commonly used methods for choosing univariate class intervals for
	mapping or other graphics purposes."""

	cran = "classInt"

	version("0.4-10", md5="dea675fe7569cbc455b10bc994d7ea1f")

	depends_on("r@2.2:", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
