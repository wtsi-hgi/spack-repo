# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class RKnitr(RPackage):
	"""A General-Purpose Package for Dynamic Report Generation in R.

	Provides a general-purpose tool for dynamic report generation in R using
	Literate Programming techniques."""

	cran = "knitr"

	license("GPL-2.0-or-later")

	version("1.45", md5="334f8f963b3d8e9e0ce5c278775cb7ec")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-evaluate@0.15:", type=("build", "run"))
	depends_on("r-highr", type=("build", "run"))
	depends_on("r-xfun@0.39:", type=("build", "run"))
	depends_on("r-yaml@2.1.19:", type=("build", "run"))
