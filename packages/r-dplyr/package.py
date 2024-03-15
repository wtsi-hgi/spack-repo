# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDplyr(RPackage):
	"""A Grammar of Data Manipulation.

	A fast, consistent tool for working with data frame like objects, both in
	memory and out of memory."""

	cran = "dplyr"

	license("MIT")

	version("1.1.4", md5="29bdf98592722336f0d07484baf2a959")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli@3.4:", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-glue@1.3.2:", type=("build", "run"))
	depends_on("r-lifecycle@1.0.3:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-pillar@1.9:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-tibble@3.2:", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
	depends_on("r-vctrs@0.6.4:", type=("build", "run"))
