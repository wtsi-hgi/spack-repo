# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyr(RPackage):
	"""Tidy Messy Data.

	Tools to help to create tidy data, where each column is a variable, each
	row is an observation, and each cell contains a single value. 'tidyr'
	contains tools for changing the shape (pivoting) and hierarchy (nesting and
	'unnesting') of a dataset, turning deeply nested lists into rectangular
	data frames ('rectangling'), and extracting values out of string columns.
	It also includes tools for working with missing values (both implicit and
	explicit)."""

	cran = "tidyr"

	license("MIT")

	version("1.3.1", md5="0491d9d3359af7baf8ad9003ce44aa1d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cli@3.4.1:", type=("build", "run"))
	depends_on("r-dplyr@1.0.10:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lifecycle@1.0.3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr@1.0.1:", type=("build", "run"))
	depends_on("r-rlang@1.1.1:", type=("build", "run"))
	depends_on("r-stringr@1.5:", type=("build", "run"))
	depends_on("r-tibble@2.1.1:", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
	depends_on("r-vctrs@0.5.2:", type=("build", "run"))
	depends_on("r-cpp11@0.4:", type=("build", "run"))
