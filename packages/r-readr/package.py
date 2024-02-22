# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReadr(RPackage):
	"""Read Rectangular Text Data.

	The goal of 'readr' is to provide a fast and friendly way to read
	rectangular data (like 'csv', 'tsv', and 'fwf'). It is designed to flexibly
	parse many types of data found in the wild, while still cleanly failing
	when data unexpectedly changes."""

	cran = "readr"

	version("2.1.5", md5="7ddf0894538a42d06035937ee6f79711")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cli@3.2:", type=("build", "run"))
	depends_on("r-clipr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-hms@0.4.1:", type=("build", "run"))
	depends_on("r-lifecycle@0.2:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-vroom@1.6:", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
	depends_on("r-tzdb@0.1.1:", type=("build", "run"))
