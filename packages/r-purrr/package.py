# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPurrr(RPackage):
	"""Functional Programming Tools.

	A complete and consistent functional programming toolkit for R."""

	cran = "purrr"

	license("MIT")

	version("1.0.2", md5="95f46bc5efc262accece5c71f81c7600")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-lifecycle@1.0.3:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-rlang@1.1.1:", type=("build", "run"))
	depends_on("r-vctrs@0.6.3:", type=("build", "run"))
